from django.urls import path
from .views import create_post, views_posts


urlpatterns = [
    path('',views_posts, name='main'),
    path('create/', create_post, name='create')
]
