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
    serializer_class = serializers.BranchSerializer

    def get_queryset(self):
        queryset = Branchs.objects.all()
        ifsc = self.request.query_params.get('ifsc',None)
        city = self.request.query_params.get('city',None)
        bank_name = self.request.query_params.get('bank_name',None)

        if ifsc is not None:
            queryset = queryset.filter(ifsc=ifsc)
        if bank_name is not None:
            bank = Banks.objects.get(name=bank_name)
            queryset = queryset.filter(bank=bank)
        if city is not None:
            queryset = queryset.filter(city=city)

        return queryset

