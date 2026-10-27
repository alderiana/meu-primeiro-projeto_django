from django.shortcuts import render, redirect 
from .models import Comentario 
from rest_framework import viewsets
from .serializers import ComentarioSerializer


def salvar_comentario(request):
    
    if request.method == 'POST':
        autor = request.POST.get('autor') 
        texto = request.POST.get('texto') 
        comentario = Comentario(autor=autor, texto=texto) # cria instância do modelo
        comentario.save() 
        
        return redirect('salvar_comentario')
        
   
    comentarios = Comentario.objects.all().order_by('-data_criacao')
    
    return render(request, 'comentarios/formulario.html', {'comentarios': comentarios})

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all().order_by('-data_criacao')
    serializer_class = ComentarioSerializer
