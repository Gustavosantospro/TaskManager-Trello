from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeLogin(request): 
    return HttpResponse('<h1>Home Login</h1>')