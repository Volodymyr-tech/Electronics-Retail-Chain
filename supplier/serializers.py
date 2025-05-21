from rest_framework import serializers
from .models import Node, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'model', 'release_date', 'node']


class NodeSerializer(serializers.ModelSerializer):

    supplier = serializers.PrimaryKeyRelatedField(
        queryset=Node.objects.all(),
        allow_null=True
    )
    products = ProductSerializer(many=True, read_only=True)
    level = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Node
        fields = [
            'id',
            'name', 'email', 'country', 'city', 'street', 'house_number',
            'supplier', 'debt', 'level', 'created_at',
            'products',
        ]
