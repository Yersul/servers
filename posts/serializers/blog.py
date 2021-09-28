from rest_framework import serializers

from posts.models import Blog


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = (
            'uuid',
            'title',
            'text',
            'author',
            'post_kind',
            'is_moderated',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')


class BlogCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Blog
        fields = (
            'uuid',
            'title',
            'text',
            'author',
            'post_kind',
            'is_moderated',
        )
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        return super().create(validated_data)


class BlogDeleteSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'
