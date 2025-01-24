from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(
        {                        
        },
        request))