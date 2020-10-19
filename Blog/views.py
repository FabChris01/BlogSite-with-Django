from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def landing(request):
    return render(request,"Blog/landing.html")

def signin(request):
    return render(request,"Blog/signin.html")

def signup(request):
    return render(request,"Blog/signup.html")

def TAC(request):
    return render(request,"Blog/TAC.html")

def selection(request):
    return render(request,"Blog/Selection.html")

def main(request):
    return render(request,"Blog/main.html")
