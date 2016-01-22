from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns("",
                       url(r'^/$', views.index, name="index"),
                       url(r'^/(?P<data>\w+)$', views.index, name="index"),
                       )
