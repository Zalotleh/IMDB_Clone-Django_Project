from django.db import models
from .constants import COUNTRIES_CHOICES
from django.contrib.auth.models import User


class Director(models.Model):
    name = models.CharField(max_length=100)
    date_of_brith = models.DateField()
    bio = models.TextField()
    country_of_birth = models.CharField(max_length=30, choices=COUNTRIES_CHOICES, default='US')

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    bio = models.TextField()
    country_of_birth = models.CharField(max_length=30, choices=COUNTRIES_CHOICES, default='US')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    description = models.TextField()
    average_rating = models.FloatField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, null=True, blank=True)
    langauge = models.CharField(null=True, blank=True, max_length=30, default="english")
    trailer_link = models.URLField(null=True, blank=True)
    genre = models.CharField(max_length=30, null=True, blank=True)
    country_of_origin = models.CharField(max_length=30, choices=COUNTRIES_CHOICES, default="US")
    actors = models.ManyToManyField(Actor, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite = models.ForeignKey(Movie, on_delete=models.DO_NOTHING, null=True, blank=True)
