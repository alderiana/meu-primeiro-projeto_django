from rest_framework import viewsets
from .models import Autor, Livro
from .serializers import AutorSerializer, LivroSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo', 'autor__nome', 'isbn', 'ano']
