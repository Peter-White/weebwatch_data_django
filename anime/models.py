from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=200)
    j_title = models.CharField(max_length=200)
    synopsis = models.TextField()
    runtime = models.IntegerField()
    type = models.CharField(max_length=15)
    release_date = models.DateField()
    duration = models.IntegerField()
    rating = models.CharField(max_length=7)
    
    class Meta:
        db_table = 'anime'
    
    def __str__(self):
        return self.title + " (" + self.release_date + ")"
    
class Genre(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField()
    anime = models.ManyToManyField(Anime)
    
    def __str__(self):
        return self.title