from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraUpdate
)

urlpatterns = [
    path('listar', HoraExtraList.as_view(), name='list_hora_extra'),
    path('editar/<int:pk>', HoraExtraUpdate.as_view(), name='edit_hora_extra'),
]