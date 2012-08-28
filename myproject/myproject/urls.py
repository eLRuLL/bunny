from django.conf.urls import patterns, include, url
from myproject.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

APPEND_SLASH = True

urlpatterns = patterns('',
    (r'^$',hello),
    (r'^hello/$',hello),
    (r'^sandra/$',sandra),
    (r'^time/$',current_datetime),
    (r'^time/plus/(\d{1,2})/$',hours_ahead),
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
