from django.shortcuts import render, redirect
from .models import *
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from tutorial import settings

def carga(request):
    i = 0
    usuarios = []
    while i < 10000:
        usuarios.append(Usuario(nombre="Usuario"+str(i)))
        i = i + 1
    Usuario.objects.bulk_create(usuarios)
    return render(request, 'usuarios.html')

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def usuarios(request):
    data = list(Usuario.objects.values())
    return JsonResponse(data, safe=False)

def borrar(request):
    Usuario.objects.all().delete()
    return redirect('/')