from rest_framework import serializers

from gun_registrer.models import Arma, Calibre, Municao, Objeto_tipo


class Calibre_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calibre
        fields = '__all__'


class Arma_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Arma
        fields = '__all__'


class Municao_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Municao
        fields = '__all__'


class Objeto_tipo_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Objeto_tipo
        fields = '__all__'
