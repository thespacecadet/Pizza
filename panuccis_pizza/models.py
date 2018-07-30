# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Order(models.Model):
    pizza_id = models.CharField(max_length=8)
    pizza_size = models.CharField(max_length=4)
    costumer_name = models.CharField(max_length=20)
    costumer_address = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s' % (self.pizza_id, self.pizza_size)

    class Meta:
        db_table = "orders"


