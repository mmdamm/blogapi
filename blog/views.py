from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model


# Create your views here.


class PostListViewSet(viewsets.ModelViewSet):
    queryset = Post.published.all()
    serializer_class = PostSerializers


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializers


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializers

    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        return Comment.objects.filter(post_id=post_id).all()



