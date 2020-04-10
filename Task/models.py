from djongo import models

# Create your models here.

class BankDetail(models.Model):
    ifsc = models.CharField(max_length=30,unique=True)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    bank_name = models.TextField()


