from django.conf.urls import include, url

from blog import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'test_project.views.home', name='home'),
    url(r'^$', views.index, name='index'),
]
