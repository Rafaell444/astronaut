from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from astronaut.apps.dashboard import urls
from astronaut.apps.home import urls

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('home.urls')),
                  path('', include('dashboard.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
