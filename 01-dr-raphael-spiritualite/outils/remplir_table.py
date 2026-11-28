"""Ouvre le .docx dans LibreOffice, met à jour la table des matières, et enregistre une copie .docx.
Usage : python3 outils/remplir_table.py entree.docx sortie.docx"""
import sys, os, time, subprocess, uno
from com.sun.star.beans import PropertyValue
def pv(n, v): p = PropertyValue(); p.Name = n; p.Value = v; return p
entree, sortie = map(os.path.abspath, sys.argv[1:3])
proc = subprocess.Popen(['soffice', '--headless', '--invisible', '--norestore',
    '--accept=socket,host=localhost,port=2002;urp;'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
ctx = None
for _ in range(60):
    try:
        local = uno.getComponentContext()
        res = local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver', local)
        ctx = res.resolve('uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext'); break
    except Exception: time.sleep(1)
desk = ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)
doc = desk.loadComponentFromURL(uno.systemPathToFileUrl(entree), '_blank', 0, (pv('Hidden', True),))
idx = doc.getDocumentIndexes(); n = idx.getCount()
for i in range(n): idx.getByIndex(i).update()
doc.storeToURL(uno.systemPathToFileUrl(sortie), (pv('FilterName', 'MS Word 2007 XML'),))
doc.close(True)
try: desk.terminate()
except Exception: pass
proc.wait(timeout=30)
print('tables mises à jour :', n)
