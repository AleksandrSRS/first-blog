from django.conf.urls import url
from django.urls import path

from . import views

#app_name = 'searchdir'
urlpatterns = [
    path('', views.searche, name="searche"),
    url(r'^result/(?P<y>\d+)/$', views.searche_detail, name="searche_detail"),
    ]