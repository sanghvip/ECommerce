from rest_framework import serializers
from .models import Order, OrderItems

from product.serializer import ProductSerializer

class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = (
            "price",
            "product",
            "quantity",
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializers(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
            "paid_amount"
        )
    def create(self,validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItems.objects.create(order=order, **items_data)
        return order
