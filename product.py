# TODO: Maybe implement time
# from datetime import datetime

import decimal

# TODO: For now keep uuid.
# Check if it's good idea to use uuid.
import uuid


class ProductBase:
    def __init__(self) -> None:
        self.product_id: int | uuid.UUID = 0
        self.name: str = ""
        self.description: str = ""
        self.price: decimal.Decimal = decimal.Decimal(0.00)
        self.quantity: int = 0


class Product(ProductBase):
    def __init__(self, **kwargs):
        super().__init__()
        # TODO: Maybe implement time.
        # self.created_at: datetime
        # self.last_modified_at: datetime
        # TODO: Maybe implement user.
        # self.writen_by: str = ""
        # self.last_modified_by: str = ""
        self.product_id = (
            kwargs.get("product_id")
            if kwargs.get("product_id") is not None
            else self.product_id
        )
        self.name = (
            kwargs.get("name")
            if kwargs.get("name") is not None
            else self.name
        )
        self.description = (
            kwargs.get("description")
            if kwargs.get("description") is not None
            else self.description
        )
        self.price = (
            kwargs.get("price")
            if kwargs.get("price") is not None
            else self.price
        )
        self.quantity = (
            kwargs.get("quantity")
            if kwargs.get("quantity") is not None
            else self.quantity
        )

    def set_product_details(self, name, product_id, description, price, quantity):
        if name is not None:
            self.name = name
        if product_id is not None:
            self.product_id = product_id
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity

    def get_product_details(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity,
        }
