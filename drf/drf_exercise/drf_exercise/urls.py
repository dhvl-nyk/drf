"""drf_exercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_exercise import views

from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^fetch_by_tag$', views.fetch_by_tag, name='fetch_by_tag'),
    url(r'^fetch_by_song$', views.fetch_by_song, name='fetch_by_song'),
    url(r'^fetch_by_artist$', views.fetch_by_artist, name='fetch_by_artist'),
    url(r'^show$', views.show, name='show'),
    url(r'^fetch_similar_songs$', views.fetch_similar_songs, name='fetch_similar_songs')
]
