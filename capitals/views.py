from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import countries
from .serializers import country_serializer

from rest_framework import viewsets

@api_view(['GET'])
def get_country(request):
    countrys = countries.objects.all()
    serializer = country_serializer(countrys, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_country(request):
    serializer = country_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


class EventViewSet(viewsets.ModelViewSet):
    queryset = countries.objects.all()
    serializer_class = country_serializer
    