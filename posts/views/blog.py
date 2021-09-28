from django.http import Http404
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters

from posts.filters import BlogFilterSet
from posts.models import Blog
from posts.serializers import BlogSerializer, BlogCreateSerializer, BlogDeleteSerializer


class BlogViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet,):
    permission_classes = [AllowAny, ]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BlogFilterSet

    def get_serializer_class(self):
        serializer_class = BlogSerializer

        if self.action == 'create':
            serializer_class = BlogCreateSerializer
        elif self.action == 'delete':
            serializer_class = BlogDeleteSerializer

        return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save
        serializer_data = BlogSerializer(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_blogs(self):
        owner = self.request.user

        try:
            instance = Blog.objects.filter(owner=owner)
            return instance
        except:
            raise Http404

    def get_object(self):
        uuid = self.kwargs['pk']
        try:
            instance = self.queryset.get(uuid=uuid)
            return instance
        except:
            raise Http404

