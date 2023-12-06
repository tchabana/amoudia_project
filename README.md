# amoudia_project

# Cahier des charges pour l'application de gestion des boutiques de Mm Amoudia

**1. Introduction**

L'objectif de ce document est de définir les spécifications du projet pour la création d'une application Django destinée à gérer les stocks et les affaires des boutiques de Mm Amoudia proposant une variété de produits tels que des voitures, des appareils électroménagers et des produits alimentaires. L'application permettra aux différents acteurs de la boutique de gérer efficacement les produits, les ventes, les commandes et les rapports.

**2. Objectifs du projet**

L'application devra offrir les fonctionnalités suivantes pour répondre aux besoins des différents acteurs :

**2.1. Administrateur**

- Gestion des utilisateurs et des rôles.
- Gestion des catégories de produits (voitures, appareils électroménagers, produits alimentaires).
- Suivi du stock de chaque produit.
- Gestion des fournisseurs et des commandes de réapprovisionnement.
- Génération de rapports sur les ventes, les stocks et les revenus.

**2.2. Gestionnaire de stock**

- Ajout, modification et suppression de produits.
- Effectué les différents inventaires.


**2.3. Vendeurs**

- Enregistrement des ventes de produits.
- Recherche et consultation des produits disponibles.
- Vérification des niveaux de stock avant de vendre un produit.
- Accès aux informations sur les produits disponibles.

**2.5. Fonctionnalités générales**

- Gestion des transactions financières, y compris les paiements et les remboursements.
- Gestion des promotions et des réductions.
- Gestion de l'historique des commandes.

**2.6. Fonctionnalités de statistiques et de rapports**

- **Statistiques sur les produits** : Permettre aux administrateurs de générer des rapports statistiques sur les ventes, les niveaux de stock, les bénéfices, etc., pour chaque produit. Cela aiderait à identifier les produits les plus performants et ceux qui nécessitent une attention particulière.Offrir la possibilité d'analyser les tendances de vente sur une période donnée pour ajuster la stratégie de réapprovisionnement et de promotion.
    
- **Suivi de la rentabilité** : Calculer la rentabilité de chaque produit en prenant en compte les coûts d'achat, les coûts de stockage et les revenus générés. Cela peut aider à prendre des décisions éclairées sur le maintien ou la suppression de produits.
    
- **Tableaux de bord personnalisables** : Permettre aux utilisateurs de personnaliser leurs tableaux de bord pour afficher les données qui leur sont pertinentes.


**2.8. Gestion des retours et des remboursements**

- Permettre aux clients de demander des retours ou des remboursements pour les produits défectueux ou insatisfaisants.

**2.9. Gestion des stocks avancée**

- **Gestion des entrepôts** : Prendre en charge la gestion de plusieurs entrepôts, si nécessaire.
    
- **Gestion des numéros de série** : Suivre les numéros de série pour les produits, notamment pour les voitures, ce qui permet de garantir la traçabilité.

**3. Exigences techniques**

- L'application sera développée en utilisant le framework Django.
- La base de données sera PostgreSQL .


**4. Suivi du projet**

Un suivi régulier du projet sera effectué pour s'assurer que les objectifs sont atteints en temps voulu. Des réunions périodiques seront organisées pour discuter des progrès, résoudre les problèmes et ajuster le cahier des charges si nécessaire.

**6. Conclusion**

Ce cahier des charges définit les grandes lignes du projet pour le développement de l'application Django de gestion   des boutiques de Mm Amoudia . 

![Diagramme de classe amoudia](https://github.com/tchabana/amoudia_project/assets/122261458/df4432f4-b7eb-49ac-972f-a981a0464df6)


## Model Relationnel
1. **Personne:**
    
    - `id_personne` (clé primaire)
    - `nom`
    - `prenom` (facultatif)
    - `adresse` (facultatif)
    - `email`  (facultatif)
    - `statut`  (client|fournisseur|client)
    - `telephone`

2. **Commande:**
    
    - `id_commande` (clé primaire)
    - `date_commande`
    - `montant_versé` (Somme totale des payement dejat effectué)
    - `id_personne` (clé étrangère référençant Personne en tant que Utilisateur)
    - `montant` (Somme de toute les ligne de commande)
    - `etat_payement` (True|False)
    
3. **Achat:**

    - `id_achat` (clé primaire)
    - `id_personne` (clé étrangère référençant Personne en tant que Fourniseur)

4. **Vente:**
    
    - `id_vente` (clé primaire)
    - `id_personne` (clé étrangère référençant Personne en tant que client)

5. **Paiement:**
    
    - `id_paiement` (clé primaire)
    - `date_paiement`
    - `montant_paiement`
    - `id_commande` (clé étrangère référençant Commande)

6. **LigneCommande:**
    
    - `id_commande` (clé étrangère référençant Commande)  }
    - `id_produit` (clé étrangère référençant Produit)    }`````PK
    - `quantite`
    - `montant_ligne_cmd`
    
7. **Produit:**
    
    - `id_produit` (clé primaire)
    - `nom_produit`
    - `description`
    - `prix_achat`
    - `prix_vente`
    - `qte_stock`
