import django.db.models
from django.contrib.postgres.fields import JSONField
from django.db import models


class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'product'


class InventoryLog(models.Model):
    # product_id = models.BigAutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100, blank=True, null=True)
    # description = models.TextField(blank=True, null=True)
    action_type = models.CharField(max_length=100, blank=True, null=False)
    # price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # quantity = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # sortable
    # snapshot = JSONField(blank=True, null=True)
    snapshot = django.db.models.JSONField(blank=True, null=True)
    # Id actiontype timesnamp snapshot
    #
    # class Meta:
    #     db_table = 'inventory_log'