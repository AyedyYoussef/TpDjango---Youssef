from django.contrib.auth.decorators import login_required
from django.shortcuts import render
@login_required
def index(request):
    context={'val':"Menu Acceuil"}
    return render(request,'index.html',context)