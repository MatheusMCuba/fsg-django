from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def apresentacao(request):
    return HttpResponse("Olá e Boa Noite!")