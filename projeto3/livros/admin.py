from django.contrib import admin
from .models import Autor, Livro
from rest_framework.authtoken.models import Token

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'isbn', 'ano', 'paginas']
    search_fields = ['titulo', 'isbn']
    list_filter = ['ano', 'autor']

admin.site.register(Token)
