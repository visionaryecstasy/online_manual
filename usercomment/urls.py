from django.urls import path

from django_auth_example.usercomment import views

app_name = 'usercomment'

urlpatterns  = [
    path('', views.NewsListView.as_view(), name='list'),
    path('post-news/', views.post_news, name='post_news'),
    path('post-comment/', views.post_comment, name='post_comments'),
    path('get-thread/', views.get_thread, name='get_thread'),
]