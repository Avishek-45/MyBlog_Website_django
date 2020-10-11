from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    short_desc = models.CharField(max_length=300, default="")
    Author = models.CharField(max_length=15, default="")
    Blog_picture = models.ImageField(default="code.jpg", null=True, blank=True)
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title


class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    content = models.TextField(default="")
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from  '+self.name+' - '+self.email


class Blogcomment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    Timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.user) + ' commented'
