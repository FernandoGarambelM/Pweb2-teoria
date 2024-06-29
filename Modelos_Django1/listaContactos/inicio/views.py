from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myHomeView(request,*args, **kwargs):
    myContext = {
        'myText' : 'Esto habla sobre nosotros',
        'myNumber' : 123,
        'myList' : [33, 44, 55],
    }
    return render(request,"home.html", myContext)
def anotherView(request):
    return HttpResponse('<h1>Esta es otra vista</h1>')