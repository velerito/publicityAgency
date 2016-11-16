from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.news_list, name='news_list'),
    url(r'^order/$', views.order, name='order'),
    url(r'^requirements/$', views.requirements, name='requirements'),
    url(r'^contact/$', views.contact, name='contact'),
]