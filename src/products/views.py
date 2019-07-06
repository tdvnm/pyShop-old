from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('helloWorld')

def new(request):
    return HttpResponse('new! ! ! ! !')
