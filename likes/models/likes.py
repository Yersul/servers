from importlib._common import _

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from users.models import CustomUser
from utils.const import LikeKindChoice
from utils.models import AbstractUUID, AbstractTimeTracker


class Like(AbstractUUID, AbstractTimeTracker):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    like_kind = models.CharField(
        choices=LikeKindChoice.choice(),
        max_length=8,
        blank=True,
        null=True,
        verbose_name=_('post')
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()