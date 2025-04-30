from django.db import models

class Theater(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=1000)
    lat = models.FloatField()
    lng = models.FloatField()
    num_of_anime = models.IntegerField()