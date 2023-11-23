from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permission import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.published.all()
    serializer_class = PostSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['author__username', 'title', 'description', 'category']
    ordering_fields = ['title', 'author__username', 'reading_time']
    ordering = ['reading_time']
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsOwnerOrSuperUser]


class TicketViewSet(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializers


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializers
    ordering = ['created']

    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        return Comment.objects.filter(post_id=post_id).all()


