from django.shortcuts import render

from django.http import HttpResponse, request 
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def webDev(request):
    return render(request,'gateway.html')

def AboutUs(request):
    return render(request,'aboutUs.html')

def Bank(request):
    return render(request,'Bank.html')