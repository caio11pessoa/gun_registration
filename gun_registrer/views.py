from rest_framework import generics

from gun_registrer import models, serializers


class Calibre(generics.ListAPIView):
    serializer_class = serializers.Calibre_serializer
    queryset = models.Calibre.objects.all()


class Arma(generics.ListAPIView):
    serializer_class = serializers.Calibre_serializer
    queryset = models.Calibre.objects.all()


class Municao(generics.ListAPIView):
    serializer_class = serializers.Calibre_serializer
    queryset = models.Calibre.objects.all()


class Objeto_tipo(generics.ListAPIView):
    serializer_class = serializers.Calibre_serializer
    queryset = models.Calibre.objects.all()
