from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import GuestUser


def home(request):
    if request.method == "GET" and 'name' in request.GET and 'location' in request.GET:
        name = request.GET['name']
        location = request.GET['location']
        
        GuestUser.objects.create(name=name, location=location)
        
        return redirect('guest')  

    return render(request, 'myapp/home.html')

def login(request):
    # return HttpResponse("Hello World! I'm Home.")
    return render(request, 'myapp/login.html')


def register(request):
    # return HttpResponse("My About page.")
    return render(request, 'myapp/register.html')

def guest(request):
    all_guests = GuestUser.objects.all()
    
    return render(request, 'myapp/guest.html', {'all_guests': all_guests})

def params(request,name,location):
    home_url = reverse('home')
    return HttpResponse(f"<h2>Welcome, {name}!</h2> <h2>Location: {location}</h2> <a href='{home_url}'>Go Back</a>")