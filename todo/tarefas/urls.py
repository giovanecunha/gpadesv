from django.conf.urls import url

from . import views

app_name = 'myapp'

urlpatterns = [
    url(r'^nova-categoria/$', views.nova_categoria, name='nova_categoria'),
]
