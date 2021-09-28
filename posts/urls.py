from django.urls import path
from rest_framework.routers import DefaultRouter

from posts.views import BlogViewSet


router = DefaultRouter()

router.register('', BlogViewSet)

urlpatterns = [

] + router.urls
