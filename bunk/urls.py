from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.bunk_options, name='bunk_options'),
    url(r'^all_bunks/$', views.all_bunks, name='all_bunks'),
    url(r'^perform_bunks/$', views.perform_bunks, name='perform_bunks'),
    url(r'^user(?P<user_id>[0-9]+)/$',views.specific_user, name='specific_user'),
]
