from django.urls import path, include
from . import views

urlpatterns = [
    path('get/', views.get_country, name='get_country'),
    path('add/', views.add_country, name='add_country'),
]