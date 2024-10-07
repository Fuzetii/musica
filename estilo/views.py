from django.shortcuts import render, redirect, get_object_or_404
from .models import Estilos

def listar_estilos(request):
    estilo = Estilos.objects.all()
    return render(request, 'listarestilo.html', {'estilo': estilo})

def cadastrar_estilo(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        Estilos.objects.create(nome=nome)
        return redirect('listar_estilos')
    return render(request, 'formestilo.html')

def editar_estilo(request, id):
    estilo = get_object_or_404(Estilos, id=id)
    if request.method == "POST":
        estilo.nome = request.POST['nome']
        estilo.save()
        return redirect('listar_estilos')
    return render(request, 'formestilo.html', {'estilo': estilo})

def excluir_estilo(request, id):
    estilo = get_object_or_404(Estilos, id=id)
    if request.method == "POST":
        estilo.delete()
        return redirect('listar_estilos')
    return render(request, 'confirmar_exclusaoestilo.html', {'estilo': estilo})
