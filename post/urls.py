"""동작 원리 요약
모델: Post와 Comment 모델은 데이터베이스 테이블에 매핑됩니다. 댓글은 외래 키를 통해 포스트와 연결됩니다.
시리얼라이저: 시리얼라이저는 모델 인스턴스를 JSON으로 변환하거나, JSON 데이터를 모델 인스턴스로 변환합니다.
뷰: 뷰는 HTTP 요청을 처리하고, 적절한 모델 데이터를 시리얼라이저를 통해 JSON 응답으로 변환하여 반환합니다.
URL 매핑: URL 패턴은 클라이언트 요청을 적절한 뷰로 라우팅하여 요청을 처리합니다."""

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
