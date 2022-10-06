from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Post, Group, Comment, Follow, User


class PostSerializer(serializers.ModelSerializer):
    '''Преобразование данных класса Post'''

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    '''Преобразование данных класса Group'''

    class Meta:
        model = Group
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    '''Преобразование данных класса Comment'''

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created',)
        read_only_fields = ('post',)


class FollorwSerializer(serializers.ModelSerializer):
    '''Преобразование данных класса Follorw'''

    user = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        read_only=True,
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        read_only=False,
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following',),
                message=('Вы уже подписаны на этого автора!'),
            )
        ]

    def validate_following(self, following):
        '''Валидация полей'''

        if following == self.context.get('request').user:
            raise serializers.ValidationError(
                'Не лучший способ накрутить подписчиков.'
                'Сам на себя - табу!'
            )
        return following
