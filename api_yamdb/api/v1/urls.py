from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, GenreViewSet, TitleViewSet,
                    ReviewViewSet, CommentViewSet,
                    UserViewSet, registration, send_jwt_token)

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet)
v1_router.register('categories',
                   CategoryViewSet, basename='categories')
v1_router.register('genres',
                   GenreViewSet, basename='genres')
v1_router.register('titles', TitleViewSet, basename='titles')
v1_router.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('auth/signup/', registration),
    path('auth/token/', send_jwt_token),
]