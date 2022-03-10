# Développement d'un site web sous Django

## Overview

l'application permet à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.

**l'application permet notamment de :**
* Demander une critique sur un livre ou un article en particulier
* Rechercher un article ou un livre intéréssant à lire, en se basant sur les critiques des autres
* De suivre l'actualité de ces followers


## Test et developpement

1. Pré-requis pour le lancement du serveur local:
   
    * Installer la dernière version de Python sur le site - https://www.python.org
    * Ouvrir l'interpréteur de commandes de Python (terminal sur Mac)
    * Créer un nouveau repertoire via la commande : ```cd mkdir projet9```
    * Initialiser un environnement virtuel via la commande : ```python -m venv```
    * Tapez dans la console et au niveau du dossier racine : ```git init```
    * Cloner le dépo via la console : ```git clone https://github.com/JulienC-Dev/P9_application_Web_Django```
    * Puis installer les dépendances: ```pip install -r requirements.txt```
    

2. Connection au serveur local http://127.0.0.1:8000/
   * Aller sur le sous-dossier - Projet9 via la commande  : ```cd Projet9```
   * lancer le serveur local via la commande : ```python manage.py runserver```
   * Ouvrir le naviguateur web puis tapez dans la barre de recherche : ```http://127.0.0.1:8000/```

## Dataset de connection 
    
La base de données db.sqlite3 intégre quelques exemples d'utilisateurs et de messages.
   
| Nom d'utilisateur  | Mots de passe |
| -------------      |:-------------:|
| Toto007            | test321321    |
| tata1000           | test321321    |
| toto10             | test321321    |
| vincent            | test321321    |

1. Connection au site admin local http://127.0.0.1:8000/admin

| Nom Admin          | Mots de passe |
| -------------      |:-------------:|
| julien2            | test321321    |


## Ressources

Vous pouvez trouver ces ressources utiles:

* Overview Django : https://www.djangoproject.com/start/overview/
* Django - Création de requêtes : https://docs.djangoproject.com/fr/4.0/topics/db/queries/#limiting-querysets


## Version 0.1

Auteur JulienC-Dev - github : https://github.com/JulienC-Dev/P9_application_Web_Django
