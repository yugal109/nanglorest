from django.shortcuts import render
from restapp.models import Menu


# Create your views here.

def home(request):
    starters=Menu.objects.filter(type="starters")
    main_dishes=Menu.objects.filter(type="main_dishes")
    drinks=Menu.objects.filter(type="drinks")
    snacks=Menu.objects.filter(type="snacks")
    specials=Menu.objects.filter(special=True)
    return render(request,"index.html",{"starters":starters,"main_dishes":main_dishes,"drinks":drinks,"snacks":snacks,"specials":specials})
