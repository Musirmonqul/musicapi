from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Actor(models.Model):

    ERKAK = 'erkak'
    AYOL = 'ayol'
    ROLE = (
        (ERKAK, 'erkak'),
        (AYOL, 'ayol')
    )

    name = models.CharField(max_length=128)
    birthdate = models.DateField()
    gender = models.CharField(max_length=5, choices=ROLE)


class Movie(models.Model):
    actors = models.ManyToManyField(Actor)
    name = models.CharField(max_length=64)
    year = models.DateField()
    imdb = models.CharField(max_length=128)
    genre = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
