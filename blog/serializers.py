from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class PostSerializers(serializers.ModelSerializer):
    user_post = User()

    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'reading_time', 'author']


class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'body', 'created']


class UserSerializers(serializers.ModelSerializer):
    user_post = PostSerializers(read_only=True,many=True)
    class Meta:
        model = User
        fields = '__all__'


class ImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'