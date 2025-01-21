from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('guest/', views.guest, name='guest'),
    path('params/<str:name>/<str:location>', views.params),
    path('login/', views.login),
    path('register/', views.register),
]