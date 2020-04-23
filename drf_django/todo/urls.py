# -*- author:caoyue -*-
from django.conf.urls import url

from todo import views

urlpatterns = [
    url(r'^todos/$', views.TodosView.as_view(), name='todos'),
    url(r'^todo/(\d+)/$', views.TodoView.as_view(), name='todo'),
    url(r'^todo/dels/$', views.TodoDelView.as_view(), name='dels')
]