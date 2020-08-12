from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('app.core.urls')),
    path('funcionarios/', include('app.funcionarios.urls')),
    path('departamentos/', include('app.departamentos.urls')),
    path('empresas/', include('app.empresas.urls')),
    path('documentos/', include('app.documentos.urls')),
    path('horas-extras/', include('app.registro_horas_extras.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
