from django.contrib import admin
from django.urls import path, include
from Blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('search/', views.search, name='search'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('signup/', views.handlesignup, name='handlesignup'),
    path('contact/', views.CONTACT, name='CONTACT'),
    # api for blog comment
    path('postcomment/', views.postcomment, name='postcomment'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),


]
