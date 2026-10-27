from django.db import models


class Comentario(models.Model):
    autor = models.CharField(max_length=100) # nome do autor do comentário (campo de texto curto)
    texto = models.TextField() # conteúdo do comentário (texto livre)
    data_criacao = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
       
        return f"{self.autor}: {self.texto[:30]}"

