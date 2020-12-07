from django.contrib import admin
from django.urls import path
from .views import Blogs, blog_detail, BlogCreateView, blog_delete, blog_update


app_name="blog"
urlpatterns = [
    path('', Blogs, name='blog'),
    path('detail/<int:my_id>/', blog_detail, name='blog-detail'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('delete/<int:my_id>/', blog_delete, name='blog-delete'),
    # path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'),
    path('update/<int:id>/', blog_update, name='blog-update'),

    

] 
