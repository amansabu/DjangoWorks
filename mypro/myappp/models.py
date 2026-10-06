from django.db import models

# Create your models here.


##Table Definition
class Person(models.Model):
    # id=models.IntegerField()
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)

class Movie(models.Model):
    movie_name=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    year=models.IntegerField()