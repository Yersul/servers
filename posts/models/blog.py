from django.utils.translation import ugettext_lazy as _
from django.db import models

from users.models import CustomUser
from utils.const import PostKindChoice
from utils.models import AbstractTimeTracker, AbstractUUID


class Blog(AbstractUUID, AbstractTimeTracker):
    title = models.CharField(max_length=20, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Владелец поста',
        related_name='title'
    )

    post_kind = models.CharField(
        choices=PostKindChoice.choice(),
        max_length=11,
        blank=True,
        null=True,
        verbose_name='Тип поста'
    )
    is_moderated = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        order_with_respect_to = 'author'
