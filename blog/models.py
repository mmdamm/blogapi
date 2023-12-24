import django.contrib.auth
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.forms import Form
from django_resized import ResizedImageField
import os
import shutil
from django.template.defaultfilters import slugify


# Create your models here.

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="account_images/", blank=True, null=True)
    job = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return self.username


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DA', 'Draft'
        PUBLISHED = 'PU', 'Published'
        REJECTED = 'RJ', 'Rejected'

    CATEGORY_CHOICES = (
        ('PL', 'Programming Language'),
        ('BC', 'Block Chain'),
        ('TL', 'Technology'),
        ('OT', 'Other')
    )
    # relations
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_posts')

    # data
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    slug = models.SlugField(max_length=100)
    # date
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    reading_time = models.PositiveIntegerField(default=None)
    object = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        for img in self.images.all():
            storage, path = img.image_file.storage, img.image_file.path
            storage.delete(path)
        super().delete(*args, **kwargs)


class Ticket(models.Model):
    name = models.CharField(max_length=25)
    message = models.TextField(max_length=250)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return f"{self.name}: {self.post}"


class ImageBlog(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image_file = models.ImageField(upload_to="post_images/", width_field=200, height_field=200)
    title_image = models.CharField(max_length=40)
    description = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def delete(self, *args, **kwargs):
        storage, path = self.image_file.storage, self.image_file.path
        storage.delete(path)
        super().delete(*args, **kwargs)




