from django.shortcuts import render
from rest_framework import viewsets
from .models import BankDetail
from . import serializers
from rest_framework import filters
import django_filters

    

class BankAPIView(viewsets.ModelViewSet):
    queryset = BankDetail.objects.all()
    serializer_class = serializers.BankSerializer
    filter_backends  = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('ifsc','bank_name','city',)

