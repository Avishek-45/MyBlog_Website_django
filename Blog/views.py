from django.shortcuts import render,HttpResponse
from .models import Blog

# Create your views here.

def home(request):
    return render(request,'Blog/index.html')

def blog(request):
    blog=Blog.objects.all()
    return render(request,'Blog/bloghome.html',{'blogs':blog})


def blogpost(request ,slug):
    blog=Blog.objects.filter(slug=slug).first()
    return render(request,'Blog/blogpost.html',{'blog':blog})


def contact(request):
    return render(request,'Blog/contact.html')

def search(request):
    return render(request,'Blog/search.html')
