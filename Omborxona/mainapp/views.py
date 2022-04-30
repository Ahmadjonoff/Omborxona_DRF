from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from stats.models import Statistika
from .serializers import *
from stats.serializers import StatSer


class ProductAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        ombor = Ombor.objects.get(user = request.user)
        products = Mahsulot.objects.filter(ombor = ombor)
        ser = MahsulotSer(products, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    def post(self, request):
        ombor = Ombor.objects.get(user=request.user)
        data = request.data
        data['ombor'] = ombor.id
        ser = MahsulotSer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        ombor = Ombor.objects.get(user=request.user)
        product = Mahsulot.objects.get(id = pk)
        if product.ombor == ombor:
            product.delete()
            return Response({"xabar":"O`chirildi"})
        return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk):
        ombor = Ombor.objects.get(user=request.user)
        product = Mahsulot.objects.get(id=pk)
        data = request.data
        data['ombor'] = ombor.id
        ser = MahsulotSer(product, data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        ombor = Ombor.objects.get(user=request.user)
        product = Mahsulot.objects.get(id=pk)
        data = request.data
        data['ombor'] = ombor.id
        ser = MahsulotSer(product, data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        ombor = Ombor.objects.get(user=request.user)
        clients = Client.objects.filter(ombor=ombor)
        ser = ClientSer(clients, many=True)
        return Response(ser.data)
    def post(self, request):
        ombor = Ombor.objects.get(user=request.user)
        data = request.data
        data['ombor'] = ombor.id
        ser = ClientSer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        ombor = Ombor.objects.get(user=request.user)
        client = Client.objects.get(id=pk)
        data = request.data
        data['ombor'] = ombor.id
        ser = ClientSer(client, data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        ombor = Ombor.objects.get(user=request.user)
        client = Client.objects.get(id=pk)
        data = request.data
        data['ombor'] = ombor.id
        ser = ClientSer(client, data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class StatsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        ombor = Ombor.objects.get(user=request.user)
        stat = Statistika.objects.filter(ombor=ombor)
        ser = StatSer(stat, many=True)
        return Response(ser.data)
    def post(self, request):
        ombor = Ombor.objects.get(user=request.user)
        data = request.data
        data['ombor'] = ombor.id
        ser = StatSer(data=data)
        if ser.is_valid():
            ser.save()
            stat = Statistika.objects.last()
            mahsulot = stat.mahsulot
            client = stat.client
            mahsulot.miqdor -= stat.miqdor
            mahsulot.save()
            client.qarz += stat.nasiya
            client.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)