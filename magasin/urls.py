from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CategoryAPIView
from .views import ProduitAPIView
from .views import AddressView


urlpatterns = [ 
    path('',views.index, name='index'),
    path('nouvFournisseur/',views.nouveauFournisseur,name='nouvFournisseur'),
    path('Catalogue/', views.Catalogue, name='Catalogue'),
    path('fournisseurs/', views.fournisseur, name='fournisseurs'),
    path('products/', views.manipprod, name='manipprod'),
    path('modifier/<int:pk>/', views.modifierProduit, name='modifierProduit'),
    path('effacer/<int:pk>/', views.effacerProduit, name='effacerProduit'),
    path('detail/<int:product_id>/', views.detailProduit, name='detailProduit'),
    path('register/',views.register, name = 'register'), 
    path('change_password/',views.change_password, name = 'change_password'), 
    path('contact/',views.cont,name='cont'),


    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view()),
     path('map/', AddressView.as_view(), name='map'),


    

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
