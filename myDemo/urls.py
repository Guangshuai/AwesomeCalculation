"""myDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from myPage import views as my_page_view

urlpatterns = [
    url(r'^$', my_page_view.home, name='home'),
    url(r'^linear-regression/$', my_page_view.linear_regression_upload, name='lr_upload'),
    url(r'^linear-regression/calculation/$', my_page_view.linear_regression_calculate, name='lr_calculate'),
    url('upload/', my_page_view.upload, name='upload'),
    url(r'^books/$', my_page_view.book_list, name='book_list'),
    url(r'^books/upload/$', my_page_view.upload_book, name='upload_book'),
    url('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
