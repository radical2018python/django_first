from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def myView(request):
 #   return HttpResponse('''<strong>Hello World from Second app</strong>
  #  <p>
   # and some more html</p>
    #''')

def myView(request):
    myContext = {'name':'Dibyalok Kumar'}
    return render (request,'myView.html',context=myContext)