# AI Sentiment Analysis System

---

## 📌 Présentation du projet

Le **AI Sentiment Analysis System** est une application modulaire développée en Python, conçue pour analyser et classifier des messages textuels clients en trois catégories de sentiments : **positif, négatif et neutre**.

Ce système simule un **pipeline simplifié d’analyse de support client**, utilisé dans des environnements de service pour prioriser les demandes entrantes et extraire des insights opérationnels à partir de données textuelles.

Ce projet met l’accent sur **l’architecture logicielle, la conception modulaire et les pipelines de traitement de données**, plutôt que sur l’utilisation de modèles de machine learning lourds.

---

## 🎯 Objectifs du projet

Les principaux objectifs sont :

- Concevoir une architecture Python scalable et modulaire
- Implémenter un pipeline NLP basé sur des règles (rule-based)
- Simuler des workflows réels d’analyse de support client
- Générer des insights exploitables à partir de données textuelles non structurées
- Appliquer les principes d’ingénierie logicielle (séparation des responsabilités, maintenabilité)

---

## 🧠 Architecture du système

Le système suit une architecture modulaire en couches, où chaque composant a une responsabilité bien définie :

### 1. Couche de présentation
- `main.py`
- Gère l’interaction utilisateur (interface CLI)
- Orchestre le workflow global du programme

---

### 2. Couche de traitement
- `sentiment.py`
- Implémente la logique de classification des sentiments basée sur des règles

---

### 3. Couche logique métier
- `utils.py`
- Implémente :
  - Système de priorité
  - Génération de réponses automatiques
  - Calcul des indicateurs de satisfaction

---

### 4. Couche de persistance des données
- `storage.py`
- Gère la sauvegarde et la lecture des données via fichiers locaux
- Assure le suivi des logs système

---

## ⚙️ Fonctionnalités principales

### 📊 Classification des sentiments
Un moteur basé sur des règles analyse les messages textuels et retourne :

- Positif 😊
- Négatif 😡
- Neutre 😐

---

### 🚨 Système de priorisation

Chaque message est associé à un niveau de priorité :

- Négatif → Haute priorité
- Neutre → Priorité moyenne
- Positif → Faible priorité

---

### 💬 Suggestions de réponses automatiques

Le système génère des réponses prédéfinies en fonction du sentiment détecté afin de simuler un assistant de support client.

---

### 📁 Persistance des données

Tous les messages analysés sont stockés dans un fichier structuré (`data.txt`) afin d’assurer la traçabilité et l’analyse historique.

---

### 📈 Module d’analyse

Le système calcule :

- Nombre total de messages traités
- Répartition des sentiments
- Taux de satisfaction client
- Indicateurs de performance simples

---

## 🧪 Limites techniques

Cette version utilise une approche **basée sur des règles (rule-based)** au lieu de modèles de machine learning.

Limites :

- Absence de compréhension sémantique avancée
- Analyse contextuelle limitée
- Dépendance aux mots-clés

---

## 🚀 Améliorations futures

### 🤖 NLP Upgrade
- Intégration de `spaCy` ou `transformers`
- Analyse contextuelle avancée des sentiments

### 🌐 Interface Web
- API REST avec Flask ou FastAPI
- Dashboard web pour visualisation des analyses

### 🗄️ Base de données
- Remplacement des fichiers par SQLite ou PostgreSQL
- Requêtes structurées et optimisation des données

### 📊 Analyse avancée
- Suivi des sentiments dans le temps
- Analyse de performance des agents
- Insights comportementaux clients
