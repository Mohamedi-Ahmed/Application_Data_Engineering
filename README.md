# Application Data Engineering

## Description
Cette application a pour but d'être un pipeline modulable pour tout le processus ETL qu'un data engineer est amené à rencontrer.
Il sera connecté à une base de donnée cloud où seront stockées les données.

---

## Intial Flow Chart

### DataFusion Hub

**Team** : Reetika, Ahmed, Elizabeth, Daria  
**Date de début** : 22/10/2024  
**Durée estimée** : 18 mois  

---

## Rétroplanning

Accéder au rétroplanning : [Lien vers Google Sheets](https://docs.google.com/spreadsheets/d/1Qso4PHCkF6IK-M4NxjYorGwiK-msX0rjo_qjLXzQbLk/edit?usp=sharing)

---

## Maquette V0

Visualiser la maquette : [Lien vers diagrams.net](https://app.diagrams.net/#G1qQJ9EB1DL29C-9kGH6J5StmeUFZBsEOW#%7B%22pageId%22%3A%223SZjbmUjb_WdZa0IrS7a%22%7D)

---

## 1ère User Story

Accéder à la User Story : [Lien vers Google Sheets](https://docs.google.com/spreadsheets/d/1UgfhhrRbLcOhaKsAVYGKv_DPYolM3URTRKUDTwrMPSE/edit?usp=sharing)

---

# Partie Mini-Application (version 0):

## Description de la mini-application
Cette mini-application permet de lire et d'explorer des fichiers aux formats CSV, TSV et Parquet. Elle fournit une interface intuitive pour visualiser les données et obtenir des informations détaillées sur la qualité des colonnes (types, valeurs nulles, etc.).

## Fonctionnalités de la mini-application

1. **Formats supportés** : CSV, TSV et Parquet.
2. **Exploration des données** :
   - Aperçu interactif des datasets.
   - Analyse des colonnes (types, valeurs nulles, uniques, etc.).
   - Visualisation graphique des valeurs nulles.
3. **Interface** :
   - Application construite avec Streamlit pour une expérience utilisateur fluide.
   - Interface claire et accessible.

---

## Comment lancer l'application

### Prérequis
- Python 3.7+
- Packages nécessaires :
  pip install streamlit polars pyarrow plotly
