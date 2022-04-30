from django.db import models
from mainapp.models import *


class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete = models.SET_NULL, null = True)
    client = models.ForeignKey(Client, on_delete = models.SET_NULL, null = True)
    miqdor = models.PositiveSmallIntegerField()
    umumiy = models.PositiveSmallIntegerField()
    tolandi = models.PositiveSmallIntegerField()
    nasiya = models.PositiveSmallIntegerField()
    sana = models.DateTimeField()
    ombor = models.ForeignKey(Ombor, on_delete = models.SET_NULL, null = True)