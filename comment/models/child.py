from django.db import models

from comment.models import Comment
from posts.models import Blog
from users.models import CustomUser
from utils.models import AbstractUUID, AbstractTimeTracker


class Child(AbstractUUID, AbstractTimeTracker):
    parent = models.ForeignKey(Comment, on_delete=models.PROTECT, blank=True, related_name='Дитя')
    comment = models.TextField(verbose_name='коммент')
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Пост')
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
