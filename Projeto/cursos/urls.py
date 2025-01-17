from django.urls import path
from .views import CursosAPIView, AvaliacoesAPIView, CursoAPIView, AvaliacaoAPIView,AvaliacaoViewSet, CursoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)


urlpatterns = [
     # Endponts de coleção
     path('cursos/', CursosAPIView.as_view(), name='cursos'),
     path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
     # Endponints individuais
     path('cursos/<int:curso_pk>', CursoAPIView.as_view(), name='curso'),
     path('avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
     # Endpoints compostos
     path('cursos/<int:cucrso_pk>/avaliacoes', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
     path('cursos/<int:cucrso_pk>/avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),
]


