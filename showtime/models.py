from django.db import models
from anime.models import Anime
from theater.models import Theater

class Showtime(models.Model):
    theater = models.ForeignKey(Theater, verbose_name="Theater", on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, verbose_name="Anime", on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    extras = models.CharField(max_length=25)