from django.contrib import admin
from django.urls import path
from mi_app.views import home, api_disponibilidad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/disponibilidad/', api_disponibilidad, name='api_disponibilidad'),
]
