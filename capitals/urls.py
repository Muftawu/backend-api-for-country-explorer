from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_country, name='get_country'),
    path('add/', views.add_country, name='add_country'),
    path('images/<int:pk>/', views.images, name='images')
]