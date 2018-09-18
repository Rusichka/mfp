from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),  #all url, who work for REST
    # url(r'social-auth/', include('social_django.urls', namespace='social')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

]
