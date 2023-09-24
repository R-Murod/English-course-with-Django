"""course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from django.urls import re_path as url
from django.views.static import serve
from course import settings
from main.views import *

urlpatterns = [
    path('', indexHandler),
    path('about/', aboutHandler),
    path('course/', courseHandler),
    path('teachers/', teachersHandler),
    path('contact/', contactHandler),
    path('search/', searchHandler),
    path('login/', loginHandler),
    path('profile/edit/', editHandler),
    path('logout/', logoutHandler),
    path('register/', registerHandler),
    path('wish/', wishHandler),
    path('teacher/<int:teacher_id>/', teacherItemHandler),
    path('course/<int:course_id>/', courseItemHandler),
    path('hello/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    })
]
