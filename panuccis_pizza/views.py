# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from panuccis_pizza.models import Order
from panuccis_pizza.serializers import PizzaSerializer
from rest_framework.generics import UpdateAPIView, DestroyAPIView


class pizza_update(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = PizzaSerializer
    lookup_field = 'pizza_id'


class pizza_delete(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = PizzaSerializer
    lookup_field = 'pizza_id'


@csrf_exempt
def pizzas_list(request):

    if request.method == 'GET':
        pizzas = Order.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PizzaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def pizza_detail(request, pizza_id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        pizza = Order.objects.get(pk=pizza_id)
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PizzaSerializer(pizza)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PizzaSerializer(pizza, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pizza.delete()
        return HttpResponse(status=204)