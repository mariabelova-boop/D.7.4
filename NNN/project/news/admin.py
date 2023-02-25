from django.contrib import admin
from .models import Post, PostCategory, Comment, Author, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Category)