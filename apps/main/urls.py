from django.conf.urls import url
from . import views

urlpatterns = [
   # This line has changed!
    url(r'^$', views.index),
]
