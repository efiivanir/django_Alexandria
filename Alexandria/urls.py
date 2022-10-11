
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from home import views as home_views


urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('home/', include('home.urls')),
    path('', home_views.home),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
                          
