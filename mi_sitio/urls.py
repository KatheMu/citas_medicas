from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mi_app.views import home, logout_view, api_disponibilidad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('api/disponibilidad/', api_disponibilidad, name='api_disponibilidad'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)