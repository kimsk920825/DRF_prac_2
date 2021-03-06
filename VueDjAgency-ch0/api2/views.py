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
    PostLikeSerializer,
)

from rest_framework.response import Response

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
    serializer_class = PostLikeSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        data = {"like": instance.like + 1}
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(data["like"])
