from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    class Media:
        css={
                "all":("css/main.css",)
        }

        js=("js/Blog.js",)

admin.site.register(Blog,BlogAdmin)