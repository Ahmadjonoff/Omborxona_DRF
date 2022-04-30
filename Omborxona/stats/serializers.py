from .models import *
from rest_framework.serializers import ModelSerializer

class StatSer(ModelSerializer):
    class Meta:
        model = Statistika
        fields = '__all__'