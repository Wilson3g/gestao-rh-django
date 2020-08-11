from django.urls import path
from .views import (
    DepartamentosList, 
    DepartamentosCreate, 
    DepartamentosEdit,
    DepartamentosDelete
)

urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_departamentos'),
    path('criar', DepartamentosCreate.as_view(), name='create_departamentos'),
    path('editar/<int:pk>', DepartamentosEdit.as_view(), name='edit_departamentos'),
    path('excluir/<int:pk>', DepartamentosDelete.as_view(), name='delete_departamentos'),
]