from django.db import models

class Personne(models.Model):
    STATUT_CHOICES = [
        ('client', 'Client'),
        ('fournisseur', 'Fournisseur'),
        ('utilisateur', 'Utilisateur'),
    ]
    id_personne = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    telephone = models.CharField(max_length=15)

class Commande(models.Model):
    id_commande = models.AutoField(primary_key=True)
    date_commande = models.DateField()
    montant_versé = models.DecimalField(max_digits=10, decimal_places=2)
    id_personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    etat_payement = models.BooleanField()

class Achat(Commande):
    id_achat = models.AutoField(primary_key=True)
    id_personne = models.ForeignKey(Personne, on_delete=models.CASCADE)

class Vente(Commande):
    id_vente = models.AutoField(primary_key=True)
    id_personne = models.ForeignKey(Personne, on_delete=models.CASCADE)

class Paiement(models.Model):
    id_paiement = models.AutoField(primary_key=True)
    date_paiement = models.DateField()
    montant_paiement = models.DecimalField(max_digits=10, decimal_places=2)
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE)

class LigneCommande(models.Model):
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    id_produit = models.ForeignKey('Produit', on_delete=models.CASCADE)
    quantite = models.IntegerField()
    montant_ligne_cmd = models.DecimalField(max_digits=10, decimal_places=2)

class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    nom_produit = models.CharField(max_length=255)
    description = models.TextField()
    prix_achat = models.DecimalField(max_digits=10, decimal_places=2)
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
    qte_stock = models.IntegerField()
