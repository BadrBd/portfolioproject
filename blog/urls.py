from django.contrib import admin
from django.urls import path
from .views import Blogs, blog_detail



urlpatterns = [
    path('', Blogs, name='blog'),
    path('detail/<int:id>', blog_detail, name='blog-detail'),
    

] 
