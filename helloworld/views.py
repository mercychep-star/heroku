from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloView(request):
    return  HttpResponse('hello there')
def anotherView(request):
    return HttpResponse('this is another view')
