from django.urls import path
from . import views

app_name = 'trips'
urlpatterns = [
    path('', views.dashboard, name='dash'),
    path('create', views.create, name='create'),
    path('<int:tid>', views.details, name='details'),
    path('<int:tid>/edit', views.edit, name='edit'),
    path('<int:tid>/remove', views.remove, name='remove'),
    path('join', views.join, name='join'),
    path('leave', views.leave, name='leave'),
    # path('edit', views.edit, name='edit'),
]