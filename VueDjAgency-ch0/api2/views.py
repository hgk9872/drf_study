from rest_framework import viewsets
from django.contrib.auth.models import User
from api2.serializers import CommentSerializer, PostSerializer, UserSerializer
from blog.models import Comment, Post

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer