from django.db import models

# Create your models here.
class Movies(models.Model):
    releasedate=models.DateField()
    moviename=models.CharField(max_length=30)
    actor=models.CharField(max_length=30)
    actress=models.CharField(max_length=30)
    rating=models.IntegerField()
