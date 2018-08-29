from django.contrib import admin

# Register your models here.
#将BlogArticles引用到当前环境
from .models import BlogArticles
#注册到admin
admin.site.register(BlogArticles)