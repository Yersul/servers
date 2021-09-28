from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from posts.models import Blog
from users.models import CustomUser
from utils.models import AbstractUUID, AbstractTimeTracker


class Comment(AbstractUUID, AbstractTimeTracker):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Пост')
    comment = models.TextField(verbose_name='коммент')
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='автор',
        related_name='author'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'
