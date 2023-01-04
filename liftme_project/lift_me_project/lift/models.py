from django.db import models

# Create your models here.

CHOICES = [
    ('Cape Town',"Cape Town"),
    ('Stellenbosch',"Stellenbosch"),
    ('Aggeneys',"Aggeneys"),
    ('Pofadder',"Pofadder"),
    ('Johannesburg',"Johannesburg"),
    ('Pretoria',"Pretoria"),
    ('Polokwane',"Polokwane"),
    ('George',"George"),
    ('Mahikeng',"Mahikeng"),
    ('Springbok',"Springbok"),
    ('Lanseria',"Lanseria"),

   
]

class Lift(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30,default=None)
    last_name = models.CharField(max_length=30,default=None)
    from_location = models.CharField(choices=CHOICES,default=None,max_length=300)
    to_location = models.CharField(choices=CHOICES,default=None,max_length=300)
    leaving_with = models.IntegerField()
    date_time_of_leaving = models.DateTimeField()
    number_of_bags = models.IntegerField()
    estimated_kms = models.IntegerField()
    willing_to_pay =models.FloatField()
  