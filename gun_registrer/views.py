from rest_framework import generics

from gun_registrer import models, serializers


class CalibreList(generics.ListCreateAPIView):
    queryset = models.Calibre.objects.all()
    serializer_class = serializers.Calibre_serializer


class CalibreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Calibre.objects.all()
    serializer_class = serializers.Calibre_serializer


class ArmaList(generics.ListCreateAPIView):
    queryset = models.Arma.objects.all()
    serializer_class = serializers.Arma_serializer


class ArmaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Arma.objects.all()
    serializer_class = serializers.Arma_serializer


class MunicaoList(generics.ListCreateAPIView):
    queryset = models.Municao.objects.all()
    serializer_class = serializers.Municao_serializer


class MunicaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Municao.objects.all()
    serializer_class = serializers.Municao_serializer


class Objeto_tipoList(generics.ListCreateAPIView):
    queryset = models.Objeto_tipo.objects.all()
    serializer_class = serializers.Objeto_tipo_serializer


class Objeto_tipoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Objeto_tipo.objects.all()
    serializer_class = serializers.Objeto_tipo_serializer


class ObjetoList(generics.ListCreateAPIView):
    queryset = models.Objeto.objects.all()
    serializer_class = serializers.Objeto_serializer


class ObjetoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Objeto.objects.all()
    serializer_class = serializers.Objeto_serializer
