
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.main.urls', namespace='main')),
    url(r'^login/', include('apps.login.urls', namespace='login')),
]
