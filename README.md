# SY09 — Consommation d'alcool chez les étudiants

Projet du cours **SY09 (Analyse de données)** de l'UTC. On étudie le jeu de données
*Student Alcohol Consumption* (deux lycées portugais, notes de maths et de portugais) pour
répondre à la question suivante :

> Dans quelle mesure les facteurs socio-éducatifs et familiaux influencent-ils la
> consommation d'alcool des étudiants, et quel est l'impact de cette consommation sur leur
> réussite scolaire ?

Le rapport final se trouve dans [`projet/projet.pdf`](projet/projet.pdf) ; le sujet donné par
l'enseignant est dans [`subject/projet.pdf`](subject/projet.pdf).

## Démarche

1. **Fusion et nettoyage** (`source/Merge.py`, `source/reponses_questions.ipynb`) — fusion des
   deux fichiers `student-mat.csv` / `student-por.csv` sur les colonnes communes aux élèves,
   typage des variables (nominales, ordinales), calcul de la réussite (`G3 >= 10`).
2. **Exploration** (`Exploration.ipynb`, `Viz.ipynb`) — statistiques descriptives, analyse
   bivariée, matrices de corrélation entre variables quantitatives (dont `Dalc`/`Walc`,
   consommation d'alcool en semaine/week-end).
3. **Réduction de dimension & clustering** (`PCA_AFTD_CAH.ipynb`, `K-means.ipynb`, `Kpp.ipynb`,
   `Kpp_clean.ipynb`) — ACP, AFTD, CAH, k-means et k-means++ (implémentation maison dans
   `td_functions/`) pour faire émerger des profils d'élèves.
4. **Classification supervisée** (`analyse_discriminante.ipynb`, `regression_lineaire.ipynb`,
   `Regerssion/shapiro.ipynb`) — LDA/QDA, naïve bayésien, KNN, régression logistique
   (linéaire et quadratique) pour prédire la réussite scolaire à partir du profil de l'élève.
5. **Synthèse** (`reponses_questions.ipynb`) — réponses structurées aux trois questions du
   projet : milieu de vie x consommation, classification des profils, prédiction de la
   réussite.

## Organisation du dépôt

```
projet/     rapport final (PDF + source LaTeX + figures + bibliographie)
subject/    sujet du projet
source/     notebooks et scripts
  td_functions/   fonctions réutilisées depuis les TDs (KNN, bayésien, validation croisée, ...)
  Regerssion/      notebook sur les tests de normalité (Shapiro)
```

## Reproduire les analyses

Les notebooks lisent les données depuis `../data/student-mat.csv` et
`../data/student-por.csv` (dataset *Student Alcohol Consumption*, disponible sur
[Kaggle](https://www.kaggle.com/datasets/uciml/student-alcohol-consumption) ou l'UCI ML
Repository). Ces fichiers ne sont pas versionnés : créer un dossier `data/` à la racine du
dépôt et y placer les deux CSV avant d'exécuter les notebooks.

Dépendances principales : `numpy`, `pandas`, `scikit-learn`, `scipy`, `matplotlib`, `seaborn`.

