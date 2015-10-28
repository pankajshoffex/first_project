from django.conf.urls import patterns, url
from core import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^signup/$', views.sign_up, name='sign_up'),
	url(r'^demo/$', views.demo, name='demo'),

	)