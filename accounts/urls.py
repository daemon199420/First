from django.conf.urls import url

from .views import (
    UserCreateAPIView,
    UserDetailAPIView,
    UserEditAPIView,
    UserLoginAPIView,
    UserListAPIView
)

urlpatterns = [
    url(r'^list/$', UserListAPIView.as_view(), name='list'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^(?P<username>[\w-]+)/$', UserDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<username>[\w-]+)/edit$', UserEditAPIView.as_view(), name='edit'),


]