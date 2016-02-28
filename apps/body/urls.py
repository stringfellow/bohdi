from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('body.views',
    
    url(r'^(?P<username>\w+)/$','user_body',name="user_body"),
    
    
)
