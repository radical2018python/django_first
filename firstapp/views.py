from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myView(request):
    return HttpResponse("Hello World Man")


def myView1(request):
    return HttpResponse("Hello World Man 1 ")

def myView2(request):
    return HttpResponse("Hello World Man 2")


def myView3(request):
    return HttpResponse("Hello World Man 3 ")