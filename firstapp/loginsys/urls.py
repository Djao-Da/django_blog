# -*- coding: utf-8 -*-

from django.conf.urls import url
from views import login_user, logout_user, register


urlpatterns = [
    url(r'^login/', login_user, name='login'),
    url(r'^logout/', logout_user, name='logout'),
    url(r'^register/', register, name='register'),
]