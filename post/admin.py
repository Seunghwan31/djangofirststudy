"""from django.contrib import admin
from .models import Post,Comment

# Repository 모델을 위한 관리자 페이지 설정
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","content","like","date")
    search_fields = ("title","content")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post","content","createAt")
    search_fields = ("content","createAt")"""
from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'like', 'date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'createAt', 'updateAt', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

