from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^musix181/login$', views.user_login, name='user_login'),
   url(r'^musix181/home/$', views.user_home, name='user_home'),
]