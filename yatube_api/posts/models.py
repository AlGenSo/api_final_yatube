from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    '''Объявляем класс Post, наследник класса Model из пакета models
    Описываем поля модели и их типы'''

    text = models.TextField(
        verbose_name='Текст публикации',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE,
        related_name='posts',
    )
    group = models.ForeignKey(
        'Group',
        verbose_name='Сообщество',
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.text


class Group(models.Model):
    '''Объявляем класс Group, наследник класса Model из пакета models
    Описываем поля модели и их типы'''

    title = models.CharField(
        verbose_name='Сообщество',
        max_length=200,
    )
    slug = models.SlugField(
        verbose_name='URL - адрес',
        unique=True,
    )
    description = models.TextField(
        verbose_name='Описание',
    )

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    '''Класс Коммент, для создания комментариев к постам.
    Описываем поля модели'''

    post = models.ForeignKey(
        Post,
        verbose_name="Комментарий",
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор комментария',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Текст комментария',
    )
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True,
    )


class Follow(models.Model):
    '''Класс подписки на авторов'''

    user = models.ForeignKey(
        User,
        verbose_name='Подписота',
        related_name='follower',
        on_delete=models.CASCADE,
    )

    following = models.ForeignKey(
        User,
        verbose_name='Автор поста',
        related_name='following',
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name="unique_follow"
            ),
        ]
