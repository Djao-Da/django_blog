"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from views import basic_one, template_two, template_three, articles, article, addlike, addcomment

urlpatterns = [
    #url(r'^1/', basic_one, name='basic_one'),
    #url(r'^2/', template_two, name='template_two'),
    #url(r'^3/', template_three, name='template_three'),
    url(r'^articles/all/$', articles, name='articles'),
#    url(r'^article/(?P<aritcle_id>\d+)/$', article, name='article'),
    url(r'^article/get/(?P<article_id>\d+)/$', article, name='article'),
    url(r'^article/addlike/(?P<article_id>\d+)/$', addlike, name='addlike'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', addcomment, name='addcomment'),
    url(r'^page/(\d+)/$', articles, name='articles'),
    url(r'^page/(?P<page_id>\d+)/$', addlike, name='addlike'),
    url(r'^', articles),

]
