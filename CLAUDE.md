# JOSEPH ACADEMY — ÉCRITURE DE LIVRES

## 1. LE CONTEXTE

Ce dépôt sert à écrire les livres que Joseph
Ahiankonou (Coach Joseph, Lomé, Togo) rédige
pour ses clients en tant que prête-plume.
Un dossier par livre. Ce fichier s'applique à
tous les livres, présents et futurs.

## 2. TON RÔLE

Tu rédiges le texte des livres. Tu écris dans
la discussion, en texte, pas dans des
documents, sauf demande explicite de Joseph.
Il valide chapitre par chapitre.

## 3. GIT — TU TRAVAILLES SEUL

Joseph ne relit pas le code et ne valide pas
les fusions. Tu es autonome sur ce dépôt.

- Tu commites et tu pousses toi-même.
- Tu fusionnes toi-même dans main. Pas de
  demande de fusion à faire valider.
- Tu pousses après chaque étape terminée, pas
  à la fin de la session. Une session peut
  s'interrompre et le travail serait perdu.
- Tu ne supprimes jamais un fichier de
  sources/ ni de manuscrit/ sans le lui
  demander d'abord.

## 4. RÈGLES DE TRAVAIL

- Un chapitre à la fois. Tu attends sa
  validation avant de passer au suivant.
- Français très simple à comprendre. Pas
  d'abréviations.
- Texte formaté : gras sur les points
  importants, titres et sous-titres distincts,
  interlignes serrés.
- Joseph travaille uniquement depuis son
  téléphone. Réponses courtes. Chaque
  manipulation expliquée étape par étape, sans
  supposer qu'il connaît l'interface.
- Il dicte à la voix, ses messages sont
  désordonnés. Réorganise ses idées en une
  structure cohérente au lieu de suivre
  l'ordre où il les a dites.
- Dis-lui franchement quand une de ses idées
  est mauvaise. Pas de flatterie.
- Si tu ne sais pas quelque chose
  précisément, dis-le. N'écris pas autour.
- Pour les décisions, propose des choix
  numérotés.
- Documents livrés en Word modifiable, jamais
  en PDF, sauf demande contraire.
- Quand un client donne un avis, ne l'accepte
  pas automatiquement : étudie-le, compare aux
  bonnes pratiques, puis garde, garde en
  partie, ou rejette — en expliquant pourquoi.

## 5. RÈGLE ABSOLUE — AUCUNE INVENTION

Le livre est signé par le client, pas par toi.

- Jamais une date, un nom, un lieu ou un
  chiffre qui ne vient pas de ses sources.
- Jamais une référence biblique, un numéro de
  psaume ou de verset qui n'a pas été vérifié
  dans le texte biblique.
- Si une information manque, tu la signales.
  Tu ne la combles pas.

## 6. CE QUI EST INTERDIT DANS L'ÉCRITURE

Formulations rejetées, à ne jamais réutiliser :

- « Demandez autour de vous… » et toute
  ouverture faible du même genre.
- « Je vais être honnête avec vous ».
  « Quelque chose vient de changer ».
  « Ce que je vois dans mes formations ».
- Les introductions qui ouvrent en posant
  trois questions au lecteur.
- Les chapitres hachés en micro-sections.
  Un livre professionnel développe.
- Les raisonnements creux. Déjà rejetés :
  « les gens échouent parce qu'ils connaissent
  trop de méthodes », « les gens savent déjà
  comment gagner de l'argent en ligne ».

## 7. STRUCTURE STANDARD D'UN LIVRE

PAGES D'OUVERTURE
Dédicace, préface, remerciements,
introduction, comment utiliser ce livre.

CORPS
Parties et chapitres. Chaque chapitre se
termine par « Faites le point » (exercices),
puis « Ce qu'il faut retenir » (résumé), puis
une transition vers le chapitre suivant.

FIN
Conclusion, annexes, à propos de l'auteur,
quatrième de couverture.

## 8. ORGANISATION DU DÉPÔT

Un dossier par livre, numéroté. Dans chacun :

sources/     les transcriptions brutes et les
             documents fournis par le client
analyse/     le plan, la structure, les
             décisions éditoriales
manuscrit/   les chapitres rédigés, un fichier
             markdown par partie
NOTES.md     les corrections et décisions du
             client, datées

## 9. TRANSCRIRE LES SOURCES AUDIO ET VIDÉO

Les clients fournissent souvent des
enregistrements, pas du texte.

Télécharger depuis Google Drive :
curl -sS -L -o video.mp4 "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t"

Extraire l'audio :
ffmpeg -i video.mp4 -ar 16000 -ac 1 -vn audio.wav

Puis supprimer la vidéo immédiatement. Jamais
deux vidéos sur le disque en même temps.

Transcrire avec faster-whisper. Modèle
« medium » au minimum — le « small » déforme
le vocabulaire spécialisé. Toujours passer un
initial_prompt contenant le vocabulaire du
livre : c'est ce qui évite qu'un terme
technique soit massacré.

Si la bibliothèque av lève
TypeError: open() got an unexpected keyword
argument 'metadata_errors', lire le WAV
toi-même et passer le tableau au modèle.

Enregistrer chaque transcription dans
sources/, puis commiter et pousser
immédiatement. Une session peut s'interrompre.
Rien ne doit être perdu.

Une transcription brute n'est jamais du
contenu de livre. C'est de la matière première
qui contient des erreurs de reconnaissance à
corriger.

## 10. PRODUIRE LE FICHIER WORD

- Un fichier markdown par partie, concaténés
  à la fin.
- Les sauts de page en OpenXML, pas en
  \newpage.
- Le titre de la table des matières dans
  l'en-tête YAML du markdown. Passé en ligne
  de commande, les accents sont corrompus.
- Table des matières automatique, jamais
  tapée à la main.
- Format A5, 148 × 210 mm, marges en miroir
  avec reliure pour un livre épais.

## 11. LES LIVRES EN COURS

### 01 — Dr Raphaël, spiritualité (EN COURS)

Chaîne YouTube « La Connaissance spirituelle ».
Enseigne l'usage des psaumes pour réclamer la
justice divine, avec la notion de convocation
spirituelle.

Sources : 11 vidéos distinctes sur Google
Drive, 10,5 Go, environ 7 heures. Aucune vidéo
ne manque. Le chiffre de 14,5 Go était le
total des 14 fichiers de départ, dont 3
doublons pesant 4,1 Go.

Les sources sont de deux natures. Neuf
enregistrements de masterclass que le Dr
Raphaël a données à des proches, enregistrées
par Joseph. Et deux vidéos déjà publiées sur
sa chaîne YouTube, qu'il a demandé d'intégrer.

Les noms de fichiers sont des étiquettes posées
par Joseph, pas une numérotation de l'auteur.
Ils ne donnent aucun ordre et aucune
indication. Il n'y a pas d'enregistrement
manquant. L'ordre du livre sera déterminé par
la logique du sujet, pas par l'ordre des
fichiers.

Les masterclass ayant été données à plusieurs
groupes, le même enseignement revient
plusieurs fois. Ces répétitions doivent être
repérées et fusionnées, jamais empilées.

Les passages propres à YouTube — accueil de
la chaîne, appel à s'abonner, renvoi vers
d'autres vidéos — sont retirés. Ils n'ont pas
leur place dans un livre.

Vocabulaire pour l'initial_prompt : Psaume,
verset, convocation spirituelle, intercession,
Écriture, prière, Dr Raphaël, La Connaissance
spirituelle.

Les 11 identifiants Drive :
1cy5GJSR7FYnIkydNV3OJa9FoH3V1F3Y6
1Vkc-WFYCelhI7sRoNkgVO0Ui6qaxLoLw
1wWn3fyktk1INV5ISD4r-bTFBxqRgFjcD
1cUZfK4buDj1Xl3QVAUyZ-iFoqftibCWX
1xxiQSzjbAb8wRL9vrRtuR-2BdPEFVibI
1HPpU0EbbzNldjOffAVrGP9GA2v0eH5of
1hVd27ToIa0-sEouoWnNDX6yWLBOT5ycZ
1_pFIHpxyIICzYjknjtt32gwYOUyXyegX
1hgB8hsu-Ahfcpm5i-pXgLjMiZ9TffsM8
1OM10GTj4tLwsrOwNYMhSWc4uoyX5a5nf
1EylQQzrkKRD4-a103DT0m2ZWAdhYF5B8

À faire, dans cet ordre : transcrire les 11
vidéos, établir l'ordre réel du contenu,
décider si cela fait un livre ou deux,
seulement ensuite rédiger.

ÉTAT AU 26 NOVEMBRE 2026 :
- Les 11 vidéos sont transcrites
  (sources/transcription-01.md à 11).
- Une fiche par vidéo (analyse/fiche-01.md
  à 11).
- Synthèse faite : analyse/SYNTHESE.md.
  Ordre réel, enseignements fusionnés,
  psaumes, creux, plan en 16 chapitres,
  verdict : un seul livre.
- Réponses de l'auteur reçues (vidéos 12 à
  14) : analyse/REPONSES-AUTEUR.md.
- Un tome par session de masterclass.
  Tome 1 = session 1 : plan en 12 chapitres
  (analyse/PLAN-TOME-1.md, option 2).
- Titre : À LA DÉCOUVERTE DES SECRETS ET
  CODES DU MONDE SPIRITUEL — Comprendre,
  pratiquer et prier pour impacter le
  physique par le spirituel.
- Style : voir NOTES.md (modèle Marcello,
  pas de numérotation, jamais de mention
  de masterclass). Chapitre 1 validé.
  Sessions 2 et 3 : l'auteur les enverra.
- En attente : le pourquoi des psaumes, son
  livre Le Pouvoir des prières mystiques.
- Corps du tome 1 terminé et validé (27 novembre
  2026) : chapitres 1 à 12, manuscrit/partie-1.md
  à partie-4.md. Monnaie des exemples : francs CFA.
- Auteur : Docteur Raphaël AGBEDISSE, Lomé,
  Rapha Ministry depuis 2021. Ne jamais
  expliquer l'origine du titre de Docteur.
- Pages d'ouverture et de fin rédigées
  (ouverture.md, fin.md). Reste : export
  Word A5, parcours et photo de l'auteur.

### 02 — Fatoumata Binta Bah, cosmétiques (EN ATTENTE)

Dite Dr Fatuma Tabinta. Formatrice en
esthétique. Trois livres confiés.

Livre 1, techniques de vente en esthétique :
terminé.
Livre 2, la connaissance des produits
cosmétiques et esthétiques : plan en 7 leçons
dicté par la cliente, à rédiger.
Livre 3, « Réussir dans les cosmétiques, de
débutant à expert » : seul le titre existe.

### 03 — Rose Ramata Djimadoum (TERMINÉ)

Cliente tchadienne, N'Djamena, Afrique
centrale et non Afrique de l'Ouest.
L'Ombre de mon Héros : livré.
Ta Route vers l'Indépendance Financière :
livré en relecture.
