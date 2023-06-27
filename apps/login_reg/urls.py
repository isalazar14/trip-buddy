from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('welcome', views.welcome, name='welcome'),
    path('logout', views.logout, name='logout'),
    path('', views.enter, name='root')
]