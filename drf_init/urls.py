from django.conf.urls import include, url
from rest_framework import routers


from django.contrib import admin



urlpatterns = [
    # Examples:
    # url(r'^$', 'drf_init.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('quick.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
