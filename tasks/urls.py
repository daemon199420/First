from django.conf.urls import url
from .views import (
    TaskCreateAPIView,
    TaskDetailAPIView,
    TaskEditAPIView,
    TaskListAPIView,
    UserTasks
)


urlpatterns = [
    url(r'^list/$', TaskListAPIView.as_view(), name='list'),
    # url(r'^create/$', TaskCreateAPIView.as_view(), name='create'),
    url(r'^(?P<name>[\w-]+)/detail$', TaskDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<name>[\w-]+)/edit$', TaskEditAPIView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/usertasks$', UserTasks.as_view(), name='usertasks'),

]




