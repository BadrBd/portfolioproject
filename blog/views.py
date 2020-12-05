from django.shortcuts import render, get_object_or_404
from .models import Blog
from .forms import BlogModelForm
from django.urls import reverse
from django.views.generic import (
CreateView,
UpdateView,
DeleteView
	)

# Create your views here.
def Blogs(request):
	blogs= Blog.objects.all()


	context={
	"object_list":blogs
	}

	return render(request, 'blog/blog.html',context)

def blog_detail(request, my_id):
	blog = Blog.objects.get(id=my_id)
	context = {
	'blog' : blog
	}
	return render(request, 'blog/blog-detail.html',context)

class BlogCreateView(CreateView):
	readonly_fields=('pub_date',)
	template_name='blog/blog-create.html'
	form_class = BlogModelForm
	queryset= Blog.objects.all()

	def get_success_url(self):
		success_url = reverse('blog:blog')
		return success_url

	

