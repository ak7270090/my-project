from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

def home(request):
    # return HttpResponse("Hello World! I'm Home.")
    return render(request, 'home.html')

def login(request):
    # return HttpResponse("Hello World! I'm Home.")
    return render(request, 'login.html')


def register(request):
    # return HttpResponse("My About page.")
    return render(request, 'register.html')

def guest(request):
    name = request.GET.get('name', 'Guest')
    location = request.GET.get('location', 'unknown')
    return render(request, 'guest.html', {'name': name, 'location':location})

def params(request,name,location):
    home_url = reverse('home')
    return HttpResponse(f"<h2>Welcome, {name}!</h2> <h2>Location: {location}</h2> <a href='{home_url}'>Go Back</a>")