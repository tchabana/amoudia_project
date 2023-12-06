from django.contrib import admin
from stock_app.models import Achat, Commande, LigneCommande, Paiement, Personne, Produit, Vente

# Register your models here.
admin.site.register(Produit)
admin.site.register(LigneCommande)
admin.site.register(Personne)
admin.site.register(Commande)
admin.site.register(Achat)
admin.site.register(Vente)
admin.site.register(Paiement)