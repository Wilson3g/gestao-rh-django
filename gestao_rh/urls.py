from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('app.core.urls')),
    path('funcionarios/', include('app.funcionarios.urls')),
    path('admin/', admin.site.urls),
]
