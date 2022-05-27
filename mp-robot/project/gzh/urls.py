from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    # 翻译
    url(r'^token/$', views.token),

]
