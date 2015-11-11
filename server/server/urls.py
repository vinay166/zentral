from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^', include('base.urls', namespace='base')),
    url(r'^inventory/', include('zentral.contrib.inventory.urls', namespace='inventory')),
    url(r'^osquery/', include('zentral.contrib.osquery.urls', namespace='osquery')),
    url(r'^santa/', include('zentral.contrib.santa.urls', namespace='santa')),
] + staticfiles_urlpatterns()
