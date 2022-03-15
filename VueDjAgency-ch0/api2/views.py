# from rest_framework import viewsets
# from django.contrib.auth.models import User
# from .serializers import UserSerializer, PostSerializer, CommentSerializer
# from blog.models import Post, Comment


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# urlpatterns = [
#     path("post/", views.PostListAPIView.as_view(), name="post-list"),
#     path("post/<int:pk>/", views.PostRetrieveAPIView.as_view(), name="post-detail"),
#     path("comment/", views.CommentCreateAPIView.as_view(), name="comment-list"),
# ]
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
)
from blog.models import Post, Comment
from api2.serializers import (
    PostListSerializer,
    PostRetrieveSerializer,
    CommentSerializer,
    CommentListSerializer,
)

# from django.contrib.auth.models import User

# from blog.models import Post, Comment


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer


class PostLikeAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
