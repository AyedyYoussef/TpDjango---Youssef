from .models import Produit, Fournisseur
from django.template import loader
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import ProduitForm, FournisseurForm, UserRegistrationForm, UserCreationForm,PasswordChangeForm
from django.shortcuts import redirect,render ,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import permission_required

from rest_framework.views import APIView
from rest_framework.response import Response
 
from magasin.models import Categorie
from magasin.serializers import CategorySerializer


from magasin.models import Produit
from magasin.serializers import ProduitSerializer

from.forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string


from django.views.generic.edit import CreateView
from .models import Address







def cont(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)


        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('contact\emails\contactform.html', {
                'name':name,
                'email':email,
                'content':content,
            })    
           


            send_mail('The contact form subject','this is the message','noreply@ayedy.com',['ayedyyoyssef@gmail.com'],html_message=html)
            return redirect('cont')
    else :
        form = ContactForm()


    return render(request,'contact/cont.html',{'form' : form})



@permission_required('magasin.majProduits.html')
def manipprod(request):
       if request.method == "POST" :
         form = ProduitForm(request.POST,request.FILES)
         if form.is_valid():
              form.save() 
              list=Produit.objects.all()
              return render(request,'magasin/vitrine.html',{'list':list})
       else : 
            form = ProduitForm() #créer formulaire vide 
            list=Produit.objects.all()
            return render(request,'magasin/majProduits.html',{'form':form,'list':list})

def Catalogue(request):	
	products= Produit.objects.all()
	context={'products':products}
	return render(request,'magasin/mesProduits.html',context )
def listprod(request):
	list=Produit.objects.all()
	return render(request,'magasin/vitrine.html',{'list':list})	


@permission_required('magasin.fournisseur.html')
def nouveauFournisseur(request):
    if request.method == "POST" :
         form = FournisseurForm(request.POST,request.FILES)
         if form.is_valid():
              form.save() 
              nouvFournisseur=Fournisseur.objects.all()
              return render(request,'magasin/vitrineF.html',{'nouvFournisseur':nouvFournisseur})
    else : 
            form = FournisseurForm() #créer formulaire vide 
            nouvFournisseur=Fournisseur.objects.all()
            return render(request,'magasin/fournisseur.html',{'form':form,'nouvFournisseur':nouvFournisseur})
    

def index(request):
     return render(request,'magasin/accueil.html' )

def fournisseur(request):
    fournisseurs = Fournisseur.objects.all()
    context = {'fournisseurs': fournisseurs}
    return render(request, 'magasin/mesFournisseurs.html', context)
@permission_required('magasin.modifierProduit.html')
def modifierProduit(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # Récupérer l'instance du modèle produit
            produit = form.save(commit=False)
            # Récupérer la nouvelle image téléchargée
            nouvelle_image = form.cleaned_data['img']
            # Si une nouvelle image a été téléchargée, la sauvegarder
            if nouvelle_image:
                produit.img = nouvelle_image
            # Sauvegarder le produit
            produit.save()
            return redirect('Catalogue')
    else:
        form = ProduitForm(instance=product)
    return render(request, 'magasin/modifierProduit.html', {'form': form})
def effacerProduit(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('Catalogue')
    return render(request, 'magasin/effacerProduit.html', {'product': product})
def detailProduit(request, product_id):
    produit = get_object_or_404(Produit, id=product_id)
    context = {'produit': produit}
    return render(request, 'magasin/detailProduit.html', context)
def register(request):
     if request.method == 'POST' :
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password1')
               user = authenticate(username=username, password=password)
               login(request,user)
               messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
               return redirect('index')
     else :
          form = UserCreationForm()
     return render(request,'registration/register.html',{'form' : form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # mise à jour de la session de l'utilisateur pour éviter qu'il ne soit déconnecté
            messages.success(request, 'Votre mot de passe a été mis à jour avec succès !')
            return redirect('login')
        else:
            messages.error(request, 'S\'il vous plaît corrigez les erreurs ci-dessous.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'registration/change_password.html', {'form': form})


class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ProduitAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Produit.objects.all()
        serializer = ProduitSerializer(categories, many=True)
        return Response(serializer.data)

  

class AddressView(CreateView):

    model = Address
    fields = ['address']
    template_name = 'magasin/map.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1IjoidHVuYWhvYmJ5IiwiYSI6ImNra3IwaDNxcTBtbzAycm81dTFpOWhvcjAifQ.8ixXcuSDUuAlDSlazSLMCA'
        context['addresses'] = Address.objects.all()
        return context


