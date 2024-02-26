# Projet de Web Scraping Python pour une Entreprise de Réparation Informatique

## Description
Ce dépôt contient le code source de mon premier projet en Python, réalisé lors de mon stage dans une entreprise spécialisée dans la réparation de postes informatiques. 
L'objectif était de créer un outil de suivi des prix des produits sur le site d'Amazon, afin d'identifier les opportunités d'achat pour l'entreprise et ses clients. 
Le projet incluait également une fonctionnalité d'envoi d'e-mail pour notifier l'équipe lorsque le prix d'un produit baissait.

## Fonctionnalités
- Scraping des données produit à partir de l'URL d'un produit Amazon.
- Extraction des informations telles que le nom du produit, le prix, la description, etc.
- Suivi de l'évolution des prix des produits au fil du temps.
- Envoi d'e-mails de notification en cas de baisse de prix.
- Stockage des données dans une base de données au format JSON pour une consultation ultérieure.

## Technologies Utilisées
- Python
- Selenium (pour l'automatisation des tâches web)
- BeautifulSoup (pour le scraping HTML)
- Matplotlib (pour la visualisation des données)
- Bibliothèque SMTP de Python (pour l'envoi d'e-mails)

## Installation
1. Clonez ce dépôt vers votre machine locale.
2. Assurez-vous d'avoir Python installé sur votre système.
3. Installez les dépendances en exécutant `pip install -r requirements.txt`.

## Utilisation
1. Exécutez le script principal `main.py`.
2. Suivez les instructions pour fournir l'URL du produit Amazon.
3. Le script effectuera le scraping des données, générera un graphique avec les informations extraites et enverra un e-mail en cas de baisse de prix.

## Auteur
[Ibra](https://github.com/ibra983)

## Licence
Ce projet est sous licence MIT - voir le fichier [LICENSE.md](LICENSE.md) pour plus de détails.
