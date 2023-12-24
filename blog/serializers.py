from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = ImageBlog
        fields = ['title_image', 'description', 'image_file', 'post']

    def create(self, validated_data):
        return ImageBlog.objects.create(**validated_data)


class PostSerializers(serializers.ModelSerializer):
    author = User()
    images = ImageSerializers(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['title', 'author', 'description', 'category', 'reading_time', 'images']


class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['name', 'body', 'created','post']


class UserSerializers(serializers.ModelSerializer):
    # user_post = PostSerializers(read_only=True,many=True)
    class Meta:
        model = CustomUser
        exclude = ['user_permissions', 'is_superuser', 'is_active']
