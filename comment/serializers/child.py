from django.http import Http404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from comment.models import Comment


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'uuid',
            'post',
            'parent',
            'comment',
            'author',
        )


class ChildCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'post',
            'parent',
            'comment',
            'created_at',
        )

    def create(self, validated_data):
        post = validated_data.pop('post', None)
        parent = validated_data.pop('parent', None)
        instance = super().create(validated_data)
        if post:
            if parent:
                instance = Comment.objects.create(**validated_data)
            else:
                raise ValidationError('couldnt find parent')
        else:
            raise Http404

        return instance


class ChildCommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'comment',
            'updated_at',
        )
        read_only_fields = ('post', 'parent',)





