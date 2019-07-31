from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^menu/$', views.menu),
    url(r'^menu/dip-sw/$', views.dipsw ,name='dipsw'),
    url(r'^menu/dip-sw/switch_set', views.switch_set ,name='switch_set'),
    url(r'^menu/alm', views.alm,name='alm'),
    #path('new_test/', views.new_test,),
    url(r'^form_samples/$', views.Lan_set, name='Lan_set'),
    url(r'^form_samples/test3/$', views.test3, name='test3'),
    path('<int:switch_id>/new/', views.new, name='new'),
    path('<int:switch_id>/', views.test, name='test'),
    path('<int:switch_id>/test2/', views.test2, name='test2'),
    ]