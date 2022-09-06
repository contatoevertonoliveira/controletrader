from django.db import models

# Create your models here.
class Eventos(models.Model):
  dataEvent = models.DateField()
  desc = models.CharField(max_length=200)
  merc = models.CharField(max_length=100)
  typeMerc = models.CharField(max_length=50)
  odds = models.CharField(max_length=50)
  invest = models.FloatField()
  retor = models.FloatField()
  pl1 = models.IntegerField()
  pl2 = models.IntegerField()
  statusTrader = models.CharField(max_length=10)
  