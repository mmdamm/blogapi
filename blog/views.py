import json

from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from .models import *
from .serializers import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import *
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.published.all()
    serializer_class = PostSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['author__username', 'title', 'description', 'category']
    ordering_fields = ['title', 'author__username', 'reading_time']
    ordering = ['reading_time']
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]


class TicketViewSet(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializers
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    ordering = ['created']
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageBlog.objects.all()
    serializer_class = ImageSerializers
    parser_classes = [FormParser, MultiPartParser]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     title_image = request.data['title_image']
    #     description = request.data['description']
    #     post = request.data['post']
    #     image_file = request.data['image_file']
    #     ImageBlog.objects.create(title_image=title_image, description=description, post_id=post, image_file=image_file)

        # file = request.data['image_file']
        # ImageBlog.objects.create(image_file=file)
        # return Response("Image updated!", status=status.HTTP_200_OK)
