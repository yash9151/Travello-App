from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'home.html', {"name":"SUNNY"})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, "result.html", {"result":res})   