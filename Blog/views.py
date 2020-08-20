from django.shortcuts import render,HttpResponse
from .models import Blog,contact
from django.contrib import messages 


# Create your views here.

def home(request):
    return render(request,'Blog/index.html')

def blog(request):
    blog=Blog.objects.all()
    return render(request,'Blog/bloghome.html',{'blogs':blog})


def blogpost(request ,slug):
    blog=Blog.objects.filter(slug=slug).first()
    return render(request,'Blog/blogpost.html',{'blog':blog})


def CONTACT(request):
    if  request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        content=request.POST['content']
        cont=contact(name=name,phone=phone,email=email,content=content)
        cont.save()
        print(name,  phone, email, content)


    return render(request,'Blog/contact.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allposts=Blog.objects.none()
    else:
        allpostsTitle=Blog.objects.filter(title__icontains=query)
        allpostsContent=Blog.objects.filter(content__icontains=query)
        allposts= allpostsTitle.union(allpostsContent)

    if allposts.count()== 0:
        messages.warning(request,"No serach result found.Please refine your query")

    return render(request,'Blog/search.html',{'blogs':allposts,'query':query})
