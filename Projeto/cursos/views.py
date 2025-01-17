# GENERIC VIEWS

from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from .permissions import EhSuperusuario

#========================== API V1 ================================================

# Para Update, Delete, etc (ações em um único registro - de indivíduo - recebe um ID)
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# Para HTTP Get e Post (endpoints de coleção)
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    
# Para Update, Delete, etc (ações em um único registro - de indivíduo - recebe um ID)
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        # kwargs.get busca infomações na URI do Path
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id = self.kwargs.get('curso_pk', pk = self.kwargs.get('avaliacai_pk')))
        return get_object_or_404(self.get_queryset(), pk = self.kwargs.get('avaliacao_pk'))
        
# Para HTTP Get e Post (endpoints de coleção)
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        # kwargs.get busca infomações na URI do Path
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id = self.kwargs.get('curso_pk'))
        return self.queryset.all()
    
    #========================== API V2 ================================================
class CursoPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    pagination_class = CursoPagination  # Definir a classe de paginação

    # Permissions
    # permission_classes = [permissions.DjangoModelPermissions]

    # Aqui usamos além de DjangoModelPermissions uma permissão personalizada (EhSuperusuario)
    permission_classes = [EhSuperusuario, permissions.DjangoModelPermissions]

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk = None):
        # curso = self.get_object()

        # Paginação na Views (Temos a paginação global feita no settings.py)
        avaliacoes = Avaliacao.objects.filter(curso_id = pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serialized = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serialized.data)

    
        serializer = AvaliacaoSerializer(avaliacoes.all(), many = True)
        # serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many = True)
        return Response(serializer.data)
    
''' VIEWSET PADRÃO
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()    
    serializer_class = AvaliacaoSerializer
'''

# VIEWSET CUSTOMIZADA
class AvaliacaoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()    
    serializer_class = AvaliacaoSerializer

