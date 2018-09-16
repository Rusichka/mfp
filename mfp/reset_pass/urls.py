from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^password_reset/$', ResetPassword.as_view(), name='password_reset'),
 #   url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    #url(r'^new_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
 #       NewPassCreate.as_view(), name='new_password'),
#    url(r'^new_password/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
