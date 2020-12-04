from django.shortcuts import render
from .models import Blog

# Create your views here.
def Blogs(request):
	blogs= Blog.objects.all()


	context={
	"object_list":blogs
	}

	return render(request, 'blog/blog.html',context)

def blog_detail(request, id):
	blog = Blog.objects.get(id=id)
	context = {
	'blog' : blog
	}
	return render(request, 'blog/blog-detail.html',context)