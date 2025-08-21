from django.shortcuts import render
from rest_framework import generics,status
from .models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

# class ProductListApiView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers

class ProductListApiView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer_data = ProductSerializers(products, many=True).data
        info = {
            'status' : 'All products shows here:',
            'products' : serializer_data
        }
        return Response(info,status=status.HTTP_200_OK)

# class ProductListCreateApiView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers

class ProductListCreateApiView(APIView):
    def post(self,request):
        dataX = request.data
        serializer = ProductSerializers(data=dataX)
        if serializer.is_valid():
            serializer.save()
            info = {
                'status' : 'it saved in Database',
                'product' : dataX
            }
            return Response(info)

class ProductListMixedUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

# class ProductDetailApiView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
#     lookup_field = 'id'

class ProductDetailApiView(APIView):
    def get(self,request,pk):
        product = Product.objects.all(id=pk)
        serializer_data = ProductSerializers(product)
        info = {
            'status' : 'All about this product is here!',
            'products' : serializer_data
        }
        return Response(info)

class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers