from django.contrib import admin
from .models import Produit,Categorie,Fournisseur,ProduitNC,Commande
from .models import Address
admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Fournisseur)
admin.site.register(ProduitNC)
admin.site.register(Commande)

admin.site.register(Address)


# Register your models here.
