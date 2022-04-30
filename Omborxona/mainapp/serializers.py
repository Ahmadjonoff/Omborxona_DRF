from rest_framework.serializers import ModelSerializer
from .models import *

class OmborSer(ModelSerializer):
    class Meta:
        model = Ombor
        fields = '__all__'

class MahsulotSer(ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

class ClientSer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'