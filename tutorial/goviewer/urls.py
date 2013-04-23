from django.conf.urls import patterns, urls

from goviewer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
