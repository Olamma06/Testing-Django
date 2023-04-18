from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def ola(request):
    return HttpResponse("Hello Ola")

def dave(request):
    return HttpResponse("Hello Dave!")

#def greet(request, name):
    #return HttpResponse(f"Hello, {name.capitalize()}")

def greet(request, name):
    return render(request,"hello/greet.html", {
        "name": name.capitalize()
    })
