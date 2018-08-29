from django.contrib import admin

# Register your models here.
#将BlogArticles引用到当前环境
from .models import BlogArticles
#注册到admin
admin.site.register(BlogArticles)
# 疑问,各个参数哪里能看到全的，raw这一行后面那个逗号
class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title","author","publish")
    list_filter = ("publish","author")
    search_fields = ('title',"body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ['publish','author']



#admin.site.unregister(BlogArticles,BlogArticlesAdmin)
#admin.site.register(BlogArticles,BlogArticlesAdmin)