from django.db import models

class member(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,null=True)
    phone=models.IntegerField(null=True)
    dob= models.DateField(null=True)
