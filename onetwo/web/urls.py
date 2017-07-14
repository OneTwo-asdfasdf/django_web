from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^contact/$', views.contact, name='contact'),
        url(r'^contact_check/$', views.contact_check, name='contact_check'),
]
