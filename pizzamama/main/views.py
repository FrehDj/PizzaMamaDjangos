from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#/ menu
def index(request):

    #return HttpResponse("La page principale")
    return render(request, 'main/index.html')
