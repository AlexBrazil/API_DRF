from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # caso não seja válido já sai da função
        serializer.save()
        # COmo é um post é retorno 2021
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Outra possível forma de resposta
        # return Response({"id" : serializer.data['id'], "curso" : serializer.data['titulo']}, status=status.HTTP_201_CREATED)

    

class AvaliacaoAPIView(APIView):
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # caso não seja válido já sai da função
        serializer.save()
        # Como é um post é retorno 2021
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
