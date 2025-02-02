from django.contrib import admin

from .models import Post, Group, Comment, Follow


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Создание класса PostAdmin, наследник модели admin.ModelAdmin'''

    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    '''Создание класса GroupAdmin, наследник модели admin.ModelAdmin'''

    list_display = (
        'title',
        'slug',
        'description',
    )
    search_fields = ('slug',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Создание класса CommentAdmin, наследник модели admin.ModelAdmin'''

    list_display = ('post', 'author', 'text', 'created',)
    list_filter = ('text', 'created',)
    search_fields = ('post', 'author', 'text',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    '''Создание класса FollowAdmin, наследник модели admin.ModelAdmin'''

    list_display = ('user', 'following',)
    list_filter = ('user', 'following',)
    search_fields = ('user', 'following',)
