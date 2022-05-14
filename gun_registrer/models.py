from django.db import models


class Calibre(models.Model):
    desc_calibre = models.CharField(max_length=45)


class Arma(models.Model):
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    quantidade_de_tiros = models.IntegerField()
    valor_estimado = models.FloatField()
    imagem = models.CharField(max_length=128)
    calibre = models.ForeignKey(
        Calibre, related_name='armas', on_delete=models.CASCADE)


class Municao(models.Model):
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    valor_estimado = models.FloatField()


class Objeto_tipo(models.Model):
    tipo_de_objeto = models.CharField(max_length=64)
