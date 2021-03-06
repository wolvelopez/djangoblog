from django.conf.urls import patterns, include, url
from django.contrib import admin
from miblog.views import *


urlpatterns = patterns('',
	url(r'^$', index),
	url(r'^summernote/', include('django_summernote.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^entradas/', include('miblog.urls')),
    url(r'^accounts/login/', 'django.contrib.auth.views.login'),
    url(r'^logout/', logout_view,  name="logout_view"),        
)
