from django.contrib import admin
from .models import Users, Post, Comment, Category, PostCategory, Tag
# Register your models here.

admin.site.register(Users)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Tag)