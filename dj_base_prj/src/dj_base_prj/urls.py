from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'dj_base_prj.views.base', name='base'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
