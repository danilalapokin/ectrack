from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    data = {"header": "Welcome to Economtrack", "message": "It's Liza and Daniel's project", "bgcol": "FF00FF"}
    return render(request, "index.html", context=data)

def about(request):
    return HttpResponse("<h2>About site</h2>")

def contact(request):
    return HttpResponse("<h1> Liza's and Daniels's project</h1>")

def products(request, productid):
    output =  "<h2>Product №{0}</h2>".format(productid)
    return HttpResponse(output)

def users(request, id, name):
    output = "<h2>User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
    return HttpResponse(output)

def ntf(request):
    return HttpResponse("LOL")

def m404(request):
    return HttpResponseNotFound("LOL")