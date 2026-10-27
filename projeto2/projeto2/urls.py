from django.contrib import admin
from django.urls import path, include  # adicionamos o include aqui

urlpatterns = [
   path('admin/', admin.site.urls),

    path('', include('cadpessoas.urls')),  # esta linha liga a página inicial à nossa API
]

