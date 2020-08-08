from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('app.core.urls')),
    path('funcionarios/', include('app.funcionarios.urls')),
    path('empresas/', include('app.empresas.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
