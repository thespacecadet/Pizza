from tastypie.resources import ModelResource
from panuccis_pizza.models import Order


class PizzaResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'