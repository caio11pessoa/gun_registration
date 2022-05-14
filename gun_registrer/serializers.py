from rest_framework import serializers

from gun_registrer.models import Calibre


class Calibre_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calibre
        fields = '__all__'
