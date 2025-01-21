# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("Hello World! I'm Home.")
    return render(request, 'home.html')


def register(request):
    # return HttpResponse("My About page.")
    return render(request, 'register.html')