"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, viewsets

from panuccis_pizza.models import Order
from panuccis_pizza.serializers import PizzaSerializer
from panuccis_pizza.views import pizza_update, pizza_delete


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = PizzaSerializer
    lookup_field = 'pizza_id'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'pizza', PizzaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^pizza/(?P<pizza_id>[0-9]+)/update/$', pizza_update.as_view(), name='update'),
    url(r'^pizza/(?P<pizza_id>[0-9]+)/delete/$', pizza_delete.as_view(), name='delete'),
    url(r'^pizza/$', PizzaViewSet, name='pizza-list')
]



