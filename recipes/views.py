from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "recipes/home.html")


def sobre(request):
    return HttpResponse("SOBRE")


def contato(request):
    return HttpResponse("CONTATO")
