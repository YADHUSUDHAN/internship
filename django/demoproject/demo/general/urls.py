from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from general.views import AboutAsView


urlpatterns = [ path(r'aboutus/',AboutAsView.as_view(),name = 'about_us_page'),
]+ static(settings.STATIC_URL,documet_root = settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,documet_root = settings.STATIC_ROOT)
