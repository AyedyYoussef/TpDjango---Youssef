from django import forms
from django.forms import ModelForm
from .models import Produit,Fournisseur
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm as AuthPasswordChangeForm

class ProduitForm(ModelForm):
    class Meta :
        model = Produit
        fields = "__all__" #pour tous les champs de la table
        #fields=['libelle','description'] #pour qulques champs
class FournisseurForm(ModelForm):
    class Meta : 
        model = Fournisseur
        fields = "__all__" #pour tous les champs de la table

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')

class PasswordChangeForm(AuthPasswordChangeForm):
    old_password = forms.CharField(
        label="Ancien mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label="Nouveau mot de passe",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="Le mot de passe doit comporter au moins 8 caractères et ne doit pas être trop courant.",
    )
    new_password2 = forms.CharField(
        label="Confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="Pour confirmer, entrez le même mot de passe que ci-dessus.",
    )

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)