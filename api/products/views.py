from rest_framework import viewsets
from .serializers import ProductSerializer
from products.models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    # queryset = Product.objects.all()
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Product.objects.filter(created_by=self.request.user)
        return Product.objects.all()

@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def product_add(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def combined(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

@api_view(['PUT', 'DELETE'])
def func(request):
    pass


