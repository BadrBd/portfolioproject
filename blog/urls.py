from django.contrib import admin
from django.urls import path
from .views import Blogs, blog_detail, BlogCreateView


app_name="blog"
urlpatterns = [
    path('', Blogs, name='blog'),
    path('detail/<int:my_id>/', blog_detail, name='blog-detail'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    

] 
