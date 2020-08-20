from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    sno= models.AutoField(primary_key=True)
    title= models.CharField(max_length=200)
    content=RichTextField(blank=True , null=True)
    short_desc=models.CharField(max_length=300,default="")
    Author=models.CharField(max_length=15,default="")
    slug=models.CharField(max_length=100)
    time=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title
