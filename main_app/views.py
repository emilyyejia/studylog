from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(reqyest):
    return HttpResponse('<h1>About the PriceCollector</h1>')