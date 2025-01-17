from django.urls import path
from .views_full import CursoAPIView, AvaliacaoAPIView

urlpatterns = [
     path('cursos/', CursoAPIView.as_view(), name='cursos'),
     path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes')
]
