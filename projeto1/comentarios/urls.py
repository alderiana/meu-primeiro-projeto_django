from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import salvar_comentario, ComentarioViewSet

router = DefaultRouter()
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('', salvar_comentario, name='salvar_comentario'),
    path('', include(router.urls)),
]
