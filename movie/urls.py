from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from movie.views import MovieViewSet, ActorViewSet, MovieActorAPIView, CommentAddAPIView, \
     CommentsAPIView, CommentDelApiView

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('actors', ActorViewSet, basename='actors')


urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:pk>/actors/', MovieActorAPIView.as_view(), name='movie_actor'),
    path('comment_delete/<int:pk>/', CommentDelApiView.as_view(), name='comment_delete'),
    path('comment_add/', CommentAddAPIView.as_view(), name='comment_add'),
    path('comments', CommentsAPIView.as_view(), name='comments'),
    path('api/auth/', obtain_auth_token)
]
