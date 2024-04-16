from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza
# Create your views here.
#/ menu
def index(request):
    pizzas = Pizza.objects.all().order_by('prix')
    pizzas_names_prices = [pizza.nom +": "+str(pizza.prix) for pizza in pizzas]
    pizzas_names_str = " DZ, ".join(pizzas_names_prices)
    #return HttpResponse("Les Pizzas : " + pizzas_names_str +" DZ")
    return render(request, 'menu/index.html', {'pizzas': pizzas})

def api_get_pizzas(request):
    pizzas = Pizza.objects.all().order_by('prix')
    json=serializers.serialize("json",pizzas)
    return HttpResponse(json)