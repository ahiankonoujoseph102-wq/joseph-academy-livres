"""Construit le fichier Word A5 du livre 01 à partir de manuscrit/.
Usage : python3 outils/construire_word.py  (depuis le dossier du livre)"""
import subprocess, re, os, copy
from docx import Document
from docx.shared import Mm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ICI = os.path.dirname(os.path.abspath(__file__))
LIVRE = os.path.dirname(ICI)
M = os.path.join(LIVRE, 'manuscrit')
SORTIE = os.path.join(LIVRE, 'livrable')
TMP = os.path.join(LIVRE, 'livrable', '_travail')
os.makedirs(TMP, exist_ok=True)

SAUT = '\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n'

def lire(n): return open(os.path.join(M, n), encoding='utf-8').read()

fin = lire('fin.md')
i = fin.index('# Quatrième de couverture')
fin_livre, quatrieme = fin[:i].rstrip().rstrip('-').rstrip(), fin[i:]

morceaux = [lire('ouverture.md')] + [lire(f'partie-{k}.md') for k in range(1, 5)] + [fin_livre]
corps = '\n\n'.join(morceaux)
corps = re.sub(r'^---\s*$', '', corps, flags=re.M)          # anciens séparateurs
corps = re.sub(r'^(# )', lambda m: SAUT + '\n' + m.group(1), corps, flags=re.M)  # saut avant chaque titre 1

yaml = '''---
title: "À LA DÉCOUVERTE DES SECRETS ET CODES DU MONDE SPIRITUEL"
subtitle: "Comprendre, pratiquer et prier pour impacter le physique par le spirituel"
author: "Docteur Raphaël AGBEDISSE"
lang: fr-FR
toc-title: "Table des matières"
---

'''
src = os.path.join(TMP, 'livre.md')
open(src, 'w', encoding='utf-8').write(yaml + corps)
open(os.path.join(TMP, 'quatrieme.md'), 'w', encoding='utf-8').write('---\nlang: fr-FR\n---\n\n' + quatrieme)

# ---------- modèle de mise en page ----------
ref = os.path.join(TMP, 'reference.docx')
subprocess.run(['pandoc', '-o', ref, '--print-default-data-file', 'reference.docx'], check=True)
d = Document(ref)
for s in d.sections:
    s.page_width, s.page_height = Mm(148), Mm(210)
    s.top_margin, s.bottom_margin = Mm(18), Mm(18)
    s.left_margin, s.right_margin = Mm(20), Mm(14)   # intérieur / extérieur
    s.gutter = Mm(5)
    s.header_distance = s.footer_distance = Mm(8)
# marges en miroir
st = d.settings.element
mm = OxmlElement('w:mirrorMargins'); st.insert(0, mm)

POL_TEXTE, POL_TITRE = 'Georgia', 'Georgia'
BLEU = RGBColor(0x14, 0x2B, 0x4F)
styles = d.styles
def regler(nom, taille=None, gras=None, couleur=None, police=POL_TEXTE, avant=None, apres=None, aligne=None, interligne=None, italique=None):
    cible = nom.replace(' ', '')
    s = next((x for x in styles if x.style_id == cible), None)
    if s is None: print('style absent :', nom); return
    f = s.font; f.name = police
    rpr = s.element.get_or_add_rPr(); rf = rpr.find(qn('w:rFonts'))
    if rf is None: rf = OxmlElement('w:rFonts'); rpr.append(rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'): rf.set(qn(a), police)
    for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:cstheme', 'w:eastAsiaTheme'):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
    if taille: f.size = Pt(taille)
    if gras is not None: f.bold = gras
    if italique is not None: f.italic = italique
    if couleur is not None: f.color.rgb = couleur
    pf = s.paragraph_format
    if avant is not None: pf.space_before = Pt(avant)
    if apres is not None: pf.space_after = Pt(apres)
    if aligne is not None: pf.alignment = aligne
    if interligne is not None: pf.line_spacing = interligne

J = WD_ALIGN_PARAGRAPH.JUSTIFY; C = WD_ALIGN_PARAGRAPH.CENTER
regler('Normal', 10.5, interligne=1.1)
for n in ('Body Text', 'First Paragraph', 'Compact'):
    regler(n, 10.5, avant=0, apres=5, aligne=J, interligne=1.1)
regler('Block Text', 10, avant=4, apres=6, italique=True, couleur=BLEU, interligne=1.1)
regler('Heading 1', 18, True, BLEU, POL_TITRE, avant=24, apres=14, aligne=C)
regler('Heading 2', 13, True, BLEU, POL_TITRE, avant=14, apres=6)
regler('Heading 3', 11.5, True, BLEU, POL_TITRE, avant=10, apres=4)
regler('Title', 22, True, BLEU, POL_TITRE, avant=90, apres=18, aligne=C)
regler('Subtitle', 13, False, BLEU, POL_TITRE, apres=60, aligne=C, italique=True)
regler('Author', 13, True, None, POL_TITRE, aligne=C)
regler('TOCHeading', 18, True, BLEU, POL_TITRE, aligne=C)
d.save(ref)

def pandoc(entree, sortie, toc):
    cmd = ['pandoc', entree, '-f', 'markdown', '-o', sortie, '--reference-doc', ref,
           '--resource-path', M]
    if toc: cmd += ['--toc', '--toc-depth=1']
    subprocess.run(cmd, check=True)

livre = os.path.join(SORTIE, 'A-la-decouverte-des-secrets-et-codes-du-monde-spirituel-tome-1.docx')
pandoc(src, livre, True)
pandoc(os.path.join(TMP, 'quatrieme.md'), os.path.join(SORTIE, 'quatrieme-de-couverture.docx'), False)

# ---------- retouches : saut de page après la page de titre et la table des matières, numéros de page ----------
d = Document(livre)
corps_xml = d.element.body
def saut(): 
    p = OxmlElement('w:p'); r = OxmlElement('w:r'); b = OxmlElement('w:br'); b.set(qn('w:type'), 'page'); r.append(b); p.append(r); return p
for p in d.paragraphs:
    if p.style.name == 'Author':
        p._p.addnext(saut()); break
# tableaux sur toute la largeur
for t in d.tables:
    tblPr = t._tbl.tblPr
    w = tblPr.find(qn('w:tblW'))
    if w is None: w = OxmlElement('w:tblW'); tblPr.append(w)
    w.set(qn('w:type'), 'pct'); w.set(qn('w:w'), '5000')
# numéro de page centré en bas
for s in d.sections:
    pied = s.footer.paragraphs[0]; pied.alignment = C
    r = pied.add_run()
    for t, v in (('begin', None), (None, 'PAGE'), ('end', None)):
        if t:
            e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), t); r._r.append(e)
        else:
            e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = v; r._r.append(e)
    r.font.size = Pt(9)
# la table des matières se met à jour à l'ouverture
upd = OxmlElement('w:updateFields'); upd.set(qn('w:val'), 'true'); d.settings.element.append(upd)
d.save(livre)
print(livre)

# ---------- table des matières remplie par LibreOffice, puis marges en miroir remises ----------
brut = os.path.join(TMP, 'livre-brut.docx')
os.replace(livre, brut)
subprocess.run(['python3', os.path.join(ICI, 'remplir_table.py'), brut, livre], check=True)
d = Document(livre)
st = d.settings.element
if st.find(qn('w:mirrorMargins')) is None:
    st.insert(0, OxmlElement('w:mirrorMargins'))
for e in st.findall(qn('w:updateFields')): st.remove(e)
d.save(livre)
print('fini :', livre)
