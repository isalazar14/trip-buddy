from django.urls import path
from . import views

app_name = 'trips'
urlpatterns = [
    path('create', views.create, name='create_trip'),
    path('<int:tid>', views.details, name='trip_details'),
    path('<int:tid>/edit', views.edit, name='edit_trip'),
    path('<int:tid>/delete', views.remove, name='delete_trip'),
    path('join', views.join, name='join_trip'),
    path('leave', views.leave, name='leave_trip'),
    path('', views.dashboard, name='dashboard'),
    # path('edit', views.edit, name='edit'),
]