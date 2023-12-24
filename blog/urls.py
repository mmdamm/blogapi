from django.urls import path, include
from . import views
from rest_framework_nested import routers
from django.contrib.auth.models import User

app_name = 'blog'
router = routers.DefaultRouter()
router.register('posts', views.PostViewSet, basename='post')
router.register('users', views.UserViewSet, basename='user')


posts_routers = routers.NestedDefaultRouter(router, 'posts', lookup='post')
posts_routers.register('comments', views.CommentViewSet, basename='post-comments')
posts_routers.register('image', views.ImageViewSet, basename='post_image')


urlpatterns = [
    path('ticket/', views.TicketViewSet.as_view(), name='ticket'),

]
urlpatterns += router.urls + posts_routers.urls
