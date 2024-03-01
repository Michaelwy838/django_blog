from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.posts_list, name="posts_list"),
    path('<slug:slug>/', views.single_post, name="single_post"),
    path('dashboard/<str:author>/', views.my_posts, name="my_posts"),
]
