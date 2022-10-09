from rest_framework import viewsets, permissions, filters, generics
# from rest_framework.views import PermissionDenied
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404

from posts.models import Post, Group
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollorwSerializer
)
from .permissions import AuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    '''view-класс реализующий операции модели Post'''

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        '''Создание поста автором'''

        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    '''view-класс реализующий операции модели Group'''

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    '''view-класс реализующий операции модели Comment'''

    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        '''Получение всех комментов к посту'''

        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        '''Создание коммента'''

        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        )


class FollowViewSet(generics.ListCreateAPIView):
    '''view-класс реализующий операции модели Follow'''

    serializer_class = FollorwSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        '''Получение всей подписоты'''

        return self.request.user.follower.all()

    def perform_create(self, serializer):
        '''Создание подписки'''

        serializer.save(user=self.request.user)
