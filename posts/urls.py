from django.urls import path
from .views import get_posts, get_profile, get_real_posts, get_real_posts_detail

urlpatterns = [
    path('posts', get_real_posts),
    path('posts/<int:pk>/', get_real_posts_detail),
    path('profile', get_profile),
    path('get_templates/', get_real_posts),

]
