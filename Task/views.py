from django.shortcuts import render
from rest_framework import viewsets
from .models import Banks,Branchs
from . import serializers
from rest_framework import filters
import django_filters

    

class BankAPIView(viewsets.ModelViewSet):
    queryset = Banks.objects.all()
    serializer_class = serializers.BankSerializer

class BranchAPIView(viewsets.ModelViewSet):
    queryset = Branchs.objects.all()
    serializer_class = serializers.BranchSerializer
    filter_backends  = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('ifsc','bank','city',)

