from django.urls import path
from django.shortcuts import render

# View functions
def homepage(req):
    return render(req, 'index.html')

def mencollection(req):
    return render(req, 'mencollection.html')

def shoes(req):
    return render(req, 'shoes.html')

def womencollection(req):
    return render(req, 'womencollection.html')

def watch(req):
    return render(req, 'watch.html')

def accessories(req):
    return render(req, 'accessoires.html')

def tshirt(req):
    return render(req, 'tshirt.html')

