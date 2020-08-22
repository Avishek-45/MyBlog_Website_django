from django.shortcuts import render,HttpResponse,redirect
from .models import Blog,contact
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


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
    return render(request,'Blog/contact.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allposts=Blog.objects.none()
    else:
        #icontains filters  the titles and contents all word or characters
        allpostsTitle=Blog.objects.filter(title__icontains=query)
        allpostsContent=Blog.objects.filter(content__icontains=query)
        allposts= allpostsTitle.union(allpostsContent)

    if allposts.count()== 0:
        messages.warning(request,"No serach result found.Please refine your query")

    return render(request,'Blog/search.html',{'blogs':allposts,'query':query})


def handlesignup(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # validation
        if len(username)>10:
            messages.error(request,"Username should be less than 10 characters!!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request,"Use alphahets and numeric characters !!!")
            return redirect('home')
        
        if pass1!=pass2:
            messages.error(request," Passwords doesnot matches. !!!")
            return redirect('home')

        # creating users
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        messages.success(request,"Successfully created account!!")
        return redirect('home')

    else:
        return HttpResponse("404 - Not Found")

def handlelogin(request):
    if request.method == 'POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request,"Successfully Logged in!!")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials!!!")
            return redirect('home')
    else:
        return HttpResponse('404 - Not Found')

def handlelogout(request):
    # if request.method == "POST":
    logout(request)
    messages.success(request,"Successfully Logged out!!")
    return redirect('home')
    # else:
    #     return HttpResponse('404 - Not Found')
