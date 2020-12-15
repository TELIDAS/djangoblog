from django.urls import path
from .views import get_real_posts, get_real_posts_detail, get_real_profile, get_real_profile_detail

urlpatterns = [
    path('posts', get_real_posts),
    path('posts/<int:pk>/', get_real_posts_detail),
    path('profile', get_real_profile),
    path('profile/<int:pk>/', get_real_profile_detail),

]
