from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# Create your views here.
#/ menu
def index(request):
    pizzas = Pizza.objects.all()
    pizzas_names_prices = [pizza.nom +": "+str(pizza.prix) for pizza in pizzas]
    pizzas_names_str = " DZ, ".join(pizzas_names_prices)
    #return HttpResponse("Les Pizzas : " + pizzas_names_str +" DZ")
    return render(request, 'menu/index.html', {'pizzas': pizzas})