from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.options, name='options'),
    url(r'^all_bunks/$', views.all_bunks, name='all_bunks'),
    url(r'^perform_bunks/$', views.perform_bunks, name='perform_bunks'),
]
