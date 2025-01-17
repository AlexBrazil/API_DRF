from rest_framework import serializers
from .models import Curso, Avaliacao
from django.db.models import Avg

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email' : {'write_only' : True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

    # O DRF permite validar campos específicos implementando métodos com o formato validate_<nome_do_campo>
    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A nota de avaliação precisa ser entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):
    # Primeira forma de relacionamento - Nested Relationship (é o menos performático, porque coloca no json tudo)
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # Segunda forma de relacionamento - HyperLinked Related Field (é mais performático  e fornece um link dos registros relacionados)
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # Terceira forma de relacioanamento - Primary Key Related Field (é mais performático  e fornece o ID dos registros relacionados) - a MAIS PERFORMÁTICA
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only = True)

    """
    Esse tipo de campo permite adicionar um campo "calculado" ou "derivado" ao serializer. 
    O valor desse campo não vem diretamente do modelo do banco de dados, mas é gerado dinamicamente por um método no 
    serializer.
    O Django Rest Framework automaticamente procura um método no serializer com o formato get_<nome_do_campo>
    """
    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        # O campo avaliacoes serve para o Relationship
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    """
        self: O serializer.
        obj: A instância do modelo Curso que está sendo serializada.
    """
    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        if media is None:
            return 0
        return round(media*2)/2