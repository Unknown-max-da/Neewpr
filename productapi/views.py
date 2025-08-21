from django.shortcuts import render
from rest_framework import generics,status
from .models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# Create your views here.

class ProductListApiView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer_data = ProductSerializers(products, many=True).data
        info = {
            'status' : 'All products shows here:',
            'products' : serializer_data
        }
        return Response(info,status=status.HTTP_200_OK)

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

class ProductDetailApiView(APIView):
    def get(self,request,pk):
        product = Product.objects.get(id=pk)
        serializer_data = ProductSerializers(product)
        info = {
            'status' : 'All about this product is here!',
            'products' : serializer_data
        }
        return Response(info)

class ProductDeleteApiView(APIView):
    def delete(self,request,pk):
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            return Response({'status : This product deleted successfully!'}, status=status.HTTP_200_OK)
        except:
            return Response({'Cannot find something like this!'}, status=status.HTTP_400_BAD_REQUEST)

class ProductUpdateApiView(APIView):
    def put(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializers(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        serializer = ProductSerializers(product, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductMixedApiView(APIView):
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        serializer_data = ProductSerializers(product).data
        info = {
            'status' : 'About this product',
            'product':serializer_data
        }
        return Response(info)
    def delete(self,request,pk):
        try:
            product=Product.objects.get(id=pk)
            product.delete()
            return Response({'status' : 'This product deleted successfully'})
        except:
            return Response({'status' : "There isn't product like that!"})
    def put(self,request,pk):
        product=get_object_or_404(Product,pk=pk)
        serializer = ProductSerializers(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializers(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)