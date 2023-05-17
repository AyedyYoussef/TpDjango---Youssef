from django.db import models
from datetime import date
import geocoder
mapbox_access_token = 'pk.eyJ1IjoidHVuYWhvYmJ5IiwiYSI6ImNra3IwaDNxcTBtbzAycm81dTFpOWhvcjAifQ.8ixXcuSDUuAlDSlazSLMCA'
# Create your models here.
class Produit(models.Model):
    catégorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey('Fournisseur', on_delete=models.CASCADE, null=True)
    TYPE_CHOICES=[  ('em','emballé'),
                    ('fr','Frais'),
                    ('cs','Conserve')]
    libellé=models.CharField(max_length=100)
    description=models.TextField(default='non définie')
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img =models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.libellé+","+self.description+","+str(self.prix)+","+self.type
class Categorie(models.Model):
    TYPE_CHOICES=[
    ('Al','Alimentaire'), ('Mb','Meuble'),
    ('Sn','Sanitaire'), ('Vs','Vaisselle'),
    ('Vt','Vêtement'),('Jx','Jouets'),
    ('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')
    ]

    name=models.CharField(max_length=50,default='Al',choices=TYPE_CHOICES)
    def __str__(self):
        return self.name
class Fournisseur(models.Model):
    nom=models.CharField(max_length=100,null=True)
    adresse=models.TextField(null=True)
    email=models.EmailField(null=True)
    telephone=models.CharField(max_length=8,null=True)
    def __str__(self):
        return (self.nom+','+self.adresse+','+self.email+','+self.telephone)
class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    
    def __str__(self):
        return "objet ProduitNC:%s"%(self.Duree_garantie)
class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)
    produits = models.ManyToManyField('Produit')

    def __str__(self):
        return str(self.dateCde) + ' - ' + str(self.totalCde)
    


class Address(models.Model):
       address = models.TextField()
       lat = models.FloatField(blank=True, null=True)
       long = models.FloatField(blank=True, null=True)

def save(self, *args, **kwargs):
        address = models.TextField()
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # returns => [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(address , self).save(*args, **kwargs)
    