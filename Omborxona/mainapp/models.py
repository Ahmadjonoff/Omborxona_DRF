from django.contrib.auth.models import User
from django.db import models

class Ombor(models.Model):
    nom = models.CharField(max_length=30)
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=13)
    joylashuv = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.nom} ({self.joylashuv})'

class Mahsulot(models.Model):
    nom = models.CharField(max_length=30)
    sana = models.DateTimeField()
    brend = models.CharField(max_length=30, blank=True)
    miqdor = models.PositiveSmallIntegerField()
    kelgan_narx = models.IntegerField()
    sotuv_narx = models.IntegerField(blank=True)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nom} ({self.brend})'

class Client(models.Model):
    nom = models.CharField(max_length=30)
    tel = models.CharField(max_length=13)
    manzil = models.CharField(max_length=30)
    qarz = models.IntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.nom} ({self.manzil})'