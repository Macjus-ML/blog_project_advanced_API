from rest_framework import generics # , permissions  # контроль авториазации на уровне view

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,) #  контроль авториазации на уровне view
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,) #  контроль авторизации на уровне view
    permission_classes = (IsAuthorOrReadOnly, ) # ползовательское разрешение
    queryset = Post.objects.all()
    serializer_class = PostSerializer
