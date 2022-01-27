from rest_framework import serializers
from django.db import models
from cores.models import Timestamp
# Create your models here.
class Movie(Timestamp):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=15)
    year  = models.IntegerField()
    
    class Meta:
        db_table = 'movies'
