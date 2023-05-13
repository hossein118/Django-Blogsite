from django.shortcuts import render
from .models import Blog , Category
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    blog_list = Blog.objects.filter(status='p')
    paginator = Paginator(blog_list, 2) 
    page_number = request.GET.get("page")
    blogs = paginator.get_page(page_number)
    context = {
        'blogs':blogs,
    }
    return render(request,'index.html',context)

def detail(request,id):
    blog = Blog.objects.get(id = id)
    context = {
        'blog':blog
    }
    return render(request,'post.html',context)


def category(request,slug):
    category = Category.objects.get(slug=slug)
    blogs = category.blogs.all()
    context = {
        'blogs':blogs,
        'category':category
    }
    return render(request,'category.html',context)
