from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def taView(request):
    my_dict = {"name":"Python World",'city':'Pune'}
    return render(request,'index.html',context=my_dict)
