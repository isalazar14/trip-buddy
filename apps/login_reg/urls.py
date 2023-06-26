from django.urls import path
from . import views

urlpatterns = [
    path('', views.enter, name='root'),
    path('register', views.register),
    path('login', views.login),
    path('welcome', views.welcome),
    path('logout', views.logout)
]