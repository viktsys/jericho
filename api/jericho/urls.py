from django.contrib import admin
from django.urls import path

from app.urls import urlspatterns as app_urls

urlpatterns = [
    path("admin/", admin.site.urls),
] + app_urls
