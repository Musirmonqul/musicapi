from django.test import TestCase, Client

from movie.models import Movie, Actor


class TestMovieViewSet(TestCase):
    def setUp(self) -> None:
        self.actor = Actor.objects.create(name='test artist', birthdate='1985-09-10')
        self.movie = Movie.objects.create(name='test movie 2', year='2021-10-16', imdb='234567892', genre='')
        self.movie.actors.add(self.actor)
        self.client = Client()

    def test_get_all_movies(self):
        response = self.client.get('/movies/')
        data = response.data
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['imdb'], '234567892')

    def test_movie_search(self):
        response = self.client.get('/movies/?search=test')
        data = response.data
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data[0]['name'], 'test movie 2')
        self.assertEquals(data[0]['imdb'], '234567892')

    def test_movie_ordering(self):
        response = self.client.get('/movies/?ordering=imdb')
        data = response.data
        self.assertEquals(data[0]['year'], '2021-10-16')
        self.assertEquals(data[0]['imdb'], '234567892')
