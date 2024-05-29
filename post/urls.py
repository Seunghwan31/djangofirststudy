"""from django.urls import path
from .views import PostList, PostDetail, CommentsList, CommentsDetail

urlpatterns = [
    # Post 관련 URL
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),

    # 댓글 관련 URL
    path('comments/', CommentsList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentsDetail.as_view(), name='comment-detail'),
]"""
"""from django.urls import path
from .views import PostList, PostDetail, CommentsList, CommentsDetail

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('comments/', CommentsList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentsDetail.as_view(), name='comment-detail'),
]
"""
from django.urls import path
from .views import PostList, PostDetail, CommentsList, CommentsDetail

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('comments/', CommentsList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentsDetail.as_view(), name='comment-detail'),
]
