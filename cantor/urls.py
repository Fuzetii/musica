from django.urls import path 
from cantor.views import listar_cantores, cadastrar_cantor, editar_cantor, excluir_cantor

urlpatterns = [
    path('', listar_cantores, name='listar_cantores'),
    path('cantor/cadastrar', cadastrar_cantor, name='cadastrar_cantor'),
    path('cantor/editar<int:id>/', editar_cantor, name='editar_cantor'),
    path('cantor/excluir<int:id>/', excluir_cantor, name='excluir_cantor')
]