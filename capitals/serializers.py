from rest_framework.serializers import ModelSerializer
from . models import countries

class country_serializer(ModelSerializer):
    class Meta:
        model = countries
        fields = '__all__'
