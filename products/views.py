from django.shortcuts import render
from .serailzers import ProductSerializer
from rest_framework.generics import  ListAPIView,CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .models import ProductsModel

class ProductViews(ListAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer

class ProductCreate(CreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer

class ProductUpdate(RetrieveUpdateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer

class ProductDelete(RetrieveDestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer

class ProductFull(RetrieveUpdateDestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer