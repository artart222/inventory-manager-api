from rest_framework import viewsets
from .models import Product, InventoryLog
from .serializers import ProductSerializer
from decimal import Decimal
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_instance = serializer.save()
        after_snapshot = {
            "id": product_instance.product_id,
            # "action_type": "CREATE",
            # "timestamp": product_instance.timestamp,
            "price": str(product_instance.price),
            "quantity": product_instance.quantity,
        }
        InventoryLog.objects.create(
            product_id=product_instance,
            action_type="CREATE",
            price=Decimal(after_snapshot['price']),
            # price=product_instance.price,
            # quantity=product_instance.quantity,
            # timestamp=product_instance.timestamp,
            snapshot=after_snapshot
        )
        return Response(serializer.data, status=201)
