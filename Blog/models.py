from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    sno= models.AutoField(primary_key=True)
    title= models.CharField(max_length=200)
    content=RichTextField(blank=True , null=True)
    short_desc=models.CharField(max_length=300,default="")
    Author=models.CharField(max_length=15,default="")
    Blog_picture=models.ImageField(default="code.jpg",upload_to="Uploaded/images",null=True,blank=True)
    slug=models.CharField(max_length=100)
    time=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title

class contact(models.Model):
        sno= models.AutoField(primary_key=True)
        name= models.CharField(max_length=100)
        phone= models.CharField(max_length=15)
        email=models.CharField(max_length=100)
        content=models.TextField(default="")
        time=models.DateTimeField(auto_now_add=True ,blank=True)

        def __str__(self):
            return 'Message from  '+self.name+' - '+self.email

