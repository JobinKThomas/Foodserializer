
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, filters

from . import models
from . import serializers
# Create your views here.

class FoodAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.FoodSerializer
    queryset = models.Food.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', 'price']
