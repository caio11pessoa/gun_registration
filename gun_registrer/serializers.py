from rest_framework import serializers

from gun_registrer.models import Arma, Calibre, Municao, Objeto_tipo


class Calibre_serializer(serializers.HyperlinkedModelSerializer):

    armas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Calibre
        fields = ('desc_calibre', 'armas')


class Arma_serializer(serializers.HyperlinkedModelSerializer):
    calibre = serializers.PrimaryKeyRelatedField(
        queryset=Calibre.objects.all(), many=False)

    class Meta:
        model = Arma
        fields = ['marca', 'modelo', 'quantidade_de_tiros',
                  'valor_estimado', 'imagem', 'calibre']


class Municao_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Municao
        fields = '__all__'


class Objeto_tipo_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Objeto_tipo
        fields = '__all__'
