from django.urls import path
from rest_framework.routers import DefaultRouter

from comment.views.child import ChildViewSet
from comment.views.comment import CommentViewSet

router = DefaultRouter()

router.register('', CommentViewSet)
router.register('', ChildViewSet)

urlpatterns = [
    path('update/', CommentViewSet.as_view({'update': 'update'})),
    path('update/child_create/', ChildViewSet.as_view({'update': 'update'})),

              ] + router.urls
