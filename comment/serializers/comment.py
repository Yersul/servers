from django.http import Http404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'uuid',
            'post',
            'comment',
            'author',
        )


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'post',
            'comment',

        )
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        post = validated_data.pop('post', None)

        if post:
            instance = Comment.objects.create(**validated_data)
            return instance


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'post'
            'comment',
            'updated_at',
        )




