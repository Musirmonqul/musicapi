from rest_framework import status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from movie.models import Movie, Actor, Comment
from movie.serializers import MovieSerializer, ActorSerializer, CommentSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['imdb', '-imdb']
    filterset_fields = ['genre']
    search_fields = ['name', 'year']

    @action(detail=True, methods=['POST'])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()

        actor = Actor.objects.create(
             name=request.data['name'],
             birthdate=request.data['birthdate'],
             gender=request.data['gender'])
        actor.save()

        movie.actors.add(actor)

        serializer = MovieSerializer(movie)
        return Response(data=serializer.data)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieActorAPIView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data['actors'])


class CommentAddAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data['user_id'] = request.user

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CommentsAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        comments = Comment.objects.all()
        return comments

    def get(self, request, *args, ** kwargs):
        comments = self.get_queryset()
        serializer = CommentSerializer(comments, many=True)
        return Response(data=serializer.data)


class CommentDelApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
