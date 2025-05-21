from rest_framework import viewsets
from .models import Node, Product
from .serializers import NodeSerializer, ProductSerializer

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all().select_related('supplier')
    serializer_class = NodeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related('node')
    serializer_class = ProductSerializer
