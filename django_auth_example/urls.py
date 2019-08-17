"""django_auth_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import users.views as user_views
import manual.views as manual_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 别忘记在顶部引入 include 函数
    url(r'^users/', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$', user_views.index, name='index'),
    url(r'chapter1/', manual_views.python_data_chapter1, name='chapter1'),
    url(r'chapter2/', manual_views.python_data_chapter2, name='chapter2'),
    url(r'chapter3/', manual_views.python_data_chapter3, name='chapter3'),
    url(r'notification_board/', manual_views.notification_board, name='notification_board'),
]
