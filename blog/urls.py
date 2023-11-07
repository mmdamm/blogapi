from django.urls import path, include
from . import views
from rest_framework_nested import routers
from django.contrib.auth.models import User

app_name = 'blog'
router = routers.DefaultRouter()
router.register('posts', views.PostListViewSet, basename='post')
router.register('ticket', views.TicketViewSet)


posts_routers = routers.NestedDefaultRouter(router, 'posts', lookup='post')
posts_routers.register('comments', views.CommentViewSet, basename='post-comments')


urlpatterns = router.urls + posts_routers.urls

#
# urlpatterns = [
#     # path('', include(router.urls))
#
#
#
# ]

