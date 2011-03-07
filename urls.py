from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

admin.site.root_path = "/admin/" # there is probably a bug in django...


urlpatterns = patterns('',
    # Example:
    # (r'^arkestra_medic/', include('arkestra_medic.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^semantic/', include('semanticeditor.urls')),
    (r"", include("contacts_and_people.urls")),
    (r"", include("arkestra_utilities.urls")),
        
    
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
)

if settings.DEBUG:
    urlpatterns+= patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )

urlpatterns += patterns('',
    url('^autocomplete/$', 'widgetry.views.search', name='widgetry-search'),
    url(r'^', include('cms.urls')),
)
