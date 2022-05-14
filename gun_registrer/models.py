from django.db import models


class Calibre(models.Model):
    desc_calibre = models.CharField(max_length=45)
