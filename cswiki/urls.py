from django.conf.urls import patterns, include, url
from cswiki import views

urlpatterns = patterns('',
  
     url(r'^index/$',views.index),
)
