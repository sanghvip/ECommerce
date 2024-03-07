from rest_framework import serializers
from .models import Order, OrderItems

frm product.serializers import ProductSerializer

class OrderItemSerializers(serializers.ModelSerializers):
    class Meta:
        model = OrderItems
        fields = (
            "price",
            "product",
            "quantity",
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

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
