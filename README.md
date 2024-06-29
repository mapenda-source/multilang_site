# Multilang Site

## Description
Ce projet est une application web Django multilingue, développée pour évaluer compétences en développement avec Django. Elle permet la gestion d'articles de blog et inclut la possibilité d'intégrer un chatbot et des fonctionnalités de recherche augmentée par intelligence artificielle (RAG).

## Table des Matières
1. [Prérequis](#prérequis)
2. [Installation](#installation)
3. [Fonctionnalités](#fonctionnalités)
4. [Internationalisation](#internationalisation)
5. [Utilisation de ChatGPT](#utilisation-de-chatgpt)
6. [Déploiement](#déploiement)
7. [Temps de Réalisation](#temps-de-réalisation)

## Prérequis
Assurez-vous d'avoir les éléments suivants installés sur votre machine :
- Python 3.10.11
- Django 5.0.6
- Git

## Installation


### Cloner le dépôt
```bash
git clone <URL_DU_DEPOT_GIT>
cd multilang_site
Créer un environnement virtuel
bash
Copier le code
python -m venv env
source env/bin/activate   # Sur Windows: env\Scripts\activate
Installer les dépendances
bash
Copier le code
pip install -r requirements.txt
Créer un superutilisateur
bash
Copier le code
python manage.py createsuperuser
Lancer le serveur de développement
bash
Copier le code
python manage.py runserver
Accédez au site à l'adresse http://127.0.0.1:8000/.

Fonctionnalités
Gestion multilingue (français et anglais)
Modèle de blog avec les champs title, content et publication_date
Vue pour afficher une liste d'articles de blog
Script add_articles.py pour ajouter des articles à la base de données
Chatbot intégré (en cours de développement)
Internationalisation
Pour ajouter d'autres langues ou modifier les traductions :

Ajoutez les langues souhaitées dans settings.py :

python
Copier le code
LANGUAGES = [
    ('en', 'English'),
    ('fr', 'Français'),
    # Ajoutez d'autres langues ici
]
Utilisez les commandes Django pour créer et compiler les fichiers de traduction :

bash
Copier le code
python manage.py makemessages -l fr
python manage.py compilemessages
Utilisation de ChatGPT
Pour la réalisation de ce projet, j'ai utilisé quelque fois ChatGPT pour obtenir  des solutions sur le sujet suivant:

Intégration de l'API pour le chatbot 
Déploiement
Le projet a ete déployé sur Render.com o

Déploiement sur Render.com
Connectez-vous à Render.com et créez un nouveau service web.
Connectez votre dépôt GitHub.
Configurez les variables d'environnement nécessaires.
Déployez l'application.
Temps de Réalisation
Installation et configuration de Django : 1 heure
Création des modèles et vues de base : 2 heures
Configuration de l'internationalisation : 7 heures
Création des templates et stylisation : 24 heures
Intégration du chatbot et de la recherche augmentée : je nai pas pu finir
Documentation et déploiement : 2 heures



### Explications des sections du `README.md`

1. **Description** : Fournit un aperçu général du projet et de ses objectifs.
2. **Table des Matières** : Aide les utilisateurs à naviguer facilement dans le document.
3. **Prérequis** : Liste les logiciels nécessaires avant de commencer l'installation.
4. **Installation** : Instructions détaillées pour configurer et lancer le projet localement.
6. **Fonctionnalités** : Liste des principales fonctionnalités de l'application, en mentionnant celles en cours de développement.
8. **Déploiement** : Guide pour déployer l'application sur une plateforme d'hébergement.
9. **Internationalisation** : Instructions pour ajouter et gérer les langues supplémentaires.
14. **Utilisation de ChatGPT** : Explique comment ChatGPT a été utilisé dans le projet.
15. **Temps de Réalisation** : Détail du temps passé sur chaque étape du projet.



# multilang_site
