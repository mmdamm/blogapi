from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class PostSerializers(serializers.ModelSerializer):
    author = User()

    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'reading_time', 'author', 'id']


class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    post = PostSerializers()

    class Meta:
        model = Comment
        fields = ['post', 'name', 'body', 'created']


class UserSerializers(serializers.ModelSerializer):
    # user_post = PostSerializers(read_only=True,many=True)
    class Meta:
        model = CustomUser
        exclude = ['user_permissions','is_superuser', 'is_active']


class ImageSerializers(serializers.ModelSerializer):
    post = PostSerializers(read_only=True, many=True)

    class Meta:
        model = Image
        fields = '__all__'