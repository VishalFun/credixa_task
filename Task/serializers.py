from rest_framework import serializers
from . import models



class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banks
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branchs
        fields = ('id','ifsc',
                  'branch','address',
                  'city','district',
                  'state','bank_name','bank')

    bank_name = serializers.SerializerMethodField('get_bank_name')
  
    def get_bank_name(self,obj):
        return obj.bank.name

  
