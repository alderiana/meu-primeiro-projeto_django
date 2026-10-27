from rest_framework import viewsets  
from .models import Pessoas          
from .serializers import PessoasSerializer  

# Alterado para ReadOnlyModelViewSet para permitir apenas GET e HEAD
class PessoasViewSet(viewsets.ReadOnlyModelViewSet):
    # Mudamos o order_by para ordenar alfabeticamente por 'nome'
    queryset = Pessoas.objects.all().order_by('nome')  
    serializer_class = PessoasSerializer              

