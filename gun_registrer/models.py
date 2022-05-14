from django.db import models


class Calibre(models.Model):
    desc_calibre = models.CharField(max_length=45)


class Objeto_tipo(models.Model):
    tipo_de_objeto = models.CharField(max_length=64)


class Objeto(models.Model):
    objeto_tipo_id = models.ForeignKey(
        Objeto_tipo, related_name='objetos', on_delete=models.CASCADE)


class Arma(models.Model):
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    quantidade_de_tiros = models.IntegerField()
    valor_estimado = models.FloatField()
    imagem = models.CharField(max_length=128)
    calibre_id = models.ForeignKey(
        Calibre, related_name='armas', on_delete=models.CASCADE)
    objeto_id = models.ForeignKey(
        Objeto, related_name='armas', on_delete=models.CASCADE)


class Municao(models.Model):
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    valor_estimado = models.FloatField()
    calibre_id = models.ForeignKey(
        Calibre, related_name='municoes', on_delete=models.CASCADE)
    objeto_id = models.ForeignKey(
        Objeto, related_name='municoes', on_delete=models.CASCADE)
