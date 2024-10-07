from django.urls import path
from.views import listar_estilos, cadastrar_estilo, editar_estilo, excluir_estilo

urlpatterns = [
    path('', listar_estilos, name='listar_estilos'),
    path('cadastrar/', cadastrar_estilo, name='cadastrar_estilo'),
    path('editar/<int:id>/', editar_estilo, name='editar_estilo'),
    path('excluir/<int:id>/', excluir_estilo, name='excluir_estilo'),
]