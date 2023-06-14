from rest_framework import serializers
from .models import Post


class PostReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def get_likes(self, obj):
        likes = list(
            like.username for like in obj.likes.get_queryset().only("username")
        )
        return likes


class PostWriteSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"
