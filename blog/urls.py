from django.urls import path
from . import views

urlpatterns=[
    path('',views.PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post-detail'),
    path('post/new/',views.PostCreateView.as_view(),name='post-create'),
    path('post/latest/',views.UserOwnPostListView.as_view(),name='user-own'),
    path('post/liked/',views.UserLikedPostListView.as_view(),name='user-liked'),
    path('post/<str:username>/',views.UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name='post-delete'),
    path('about/',views.about,name='blog-about'),
    path('announcements/',views.announcement,name='blog-announcement'),
    path('like/<int:pk>/',views.like_post, name='post-like'),
    path('dislike/<int:pk>/',views.dislike_post, name='post-dislike')
]