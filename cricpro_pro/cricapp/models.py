from django.db import models
class Register(models.model):
    player_name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    DOB=models.DateField()
    role=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    mobile=models.BigIntegerField()



