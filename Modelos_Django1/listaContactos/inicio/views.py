from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myHomeView(request,*args, **kwargs):
    return render(request,"home.html",{})
def anotherView(request):
    return HttpResponse('<h1>Esta es otra vista</h1>')