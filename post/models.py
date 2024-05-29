"""from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(        
        max_length=150,
        default="",
        blank=True,
        null=True,
        )
    content= models.TextField(
        max_length=500,
        default="",
        blank=True,
        null=True,
    )
    like = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE)
    content=models.TextField(
        max_length=500,
        default="",
        blank=True,
        null=True,
    )
    createAt= models.DateField(auto_now_add=True)
    updateAt=models.DateField(auto_now=True)"""
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150, default="", blank=True, null=True)
    content = models.TextField(max_length=500, default="", blank=True, null=True)
    like = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=500, default="", blank=True, null=True)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    """Post 모델은 포스트를 나타내고, Comment 모델은 각 포스트에 대한 댓글을 나타냈습니다.
Comment 모델의 post 필드는 외래 키로, 댓글이 특정 포스트에 연결되도록 했습니다. related_name='comments'는 역참조를 위한 설정입니다.
"""
