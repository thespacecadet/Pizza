from rest_framework import serializers
from panuccis_pizza.models import Order


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('pizza_id', 'pizza_size', 'costumer_name', 'costumer_address')
