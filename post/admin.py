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
"""Post 모델은 포스트를 나타내고, Comment 모델은 각 포스트에 대한 댓글을 나타냈습니다.
Comment 모델의 post 필드는 외래 키로, 댓글이 특정 포스트에 연결되도록 했습니다. related_name='comments'는 역참조를 위한 설정입니다.
"""
