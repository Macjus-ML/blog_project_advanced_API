from django.contrib.auth import get_user_model

# # На основе представлений
# from rest_framework import generics  # , permissions  # контроль авториазации на уровне view
#
#
# from .models import Post
# from .serializers import PostSerializer, UserSerializer
# from .permissions import IsAuthorOrReadOnly
#
#
# class PostList(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,) #  контроль авториазации на уровне view
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticated,) #  контроль авторизации на уровне view
#     permission_classes = (IsAuthorOrReadOnly,)  # ползовательское разрешение
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


#  На основе классов представлений

from rest_framework import viewsets

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
