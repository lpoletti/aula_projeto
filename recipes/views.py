from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HTTP RESPONSE
    return HttpResponse('uma linda string')

def contato(request):
    # return HTTP RESPONSE
    return HttpResponse('CONTATO')

def sobre(request):
    # return HTTP RESPONSE
    return HttpResponse('SOBRE')