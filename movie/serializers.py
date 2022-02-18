from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Movie, Actor, Comment


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', 'gender', 'birthdate')

    # def validate_birthdate(self, value):
    #
    #     if not value.gt('01.01.1950'):
    #         raise ValidationError(detail='birthdate is greater than 01.01.1950')
    #     return value


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('actors', 'name', 'year', 'genre', 'imdb')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('movie_id', 'text',)
