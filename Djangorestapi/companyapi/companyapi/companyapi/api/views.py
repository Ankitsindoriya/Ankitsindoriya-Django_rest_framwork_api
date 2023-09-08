from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company
from api.serializers import Companyserializers

# Create your views here.
class Companyviewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = Companyserializers
