from rest_framework import serializers

from gun_registrer.models import Arma, Calibre, Municao, Objeto, Objeto_tipo


class Objeto_tipo_serializer(serializers.HyperlinkedModelSerializer):
    objetos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Objeto_tipo
        fields = ('objetos', 'tipo_de_objeto')


class Objeto_serializer(serializers.HyperlinkedModelSerializer):
    objeto_tipo_id = serializers.PrimaryKeyRelatedField(
        queryset=Objeto_tipo.objects.all(), many=False)
    armas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    municoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Objeto
        fields = ['objeto_tipo_id', 'armas', 'municoes']


class Calibre_serializer(serializers.HyperlinkedModelSerializer):

    armas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    municoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Calibre
        fields = ('desc_calibre', 'armas', 'municoes')


class Arma_serializer(serializers.HyperlinkedModelSerializer):
    calibre_id = serializers.PrimaryKeyRelatedField(
        queryset=Calibre.objects.all(), many=False)
    objeto_id = serializers.PrimaryKeyRelatedField(
        queryset=Objeto.objects.all(), many=False)

    class Meta:
        model = Arma
        fields = ['marca', 'modelo', 'quantidade_de_tiros',
                  'valor_estimado', 'imagem', 'calibre_id', 'objeto_id']


class Municao_serializer(serializers.HyperlinkedModelSerializer):
    calibre_id = serializers.PrimaryKeyRelatedField(
        queryset=Calibre.objects.all(), many=False)
    objeto_id = serializers.PrimaryKeyRelatedField(
        queryset=Objeto.objects.all(), many=False)

    class Meta:
        model = Municao
        fields = ['marca', 'modelo',
                  'valor_estimado', 'calibre_id', 'objeto_id']
