from abc import ABC
# TODO: Maybe implement time
# from datetime import datetime


class ProductBase:
    def __init__(self) -> None:
        self.product_id: int | str = 0
        self.name: str = ""
        self.description: str = ""
        self.price: float = 0.0
        self.quantity: int = 0


class Product(ABC, ProductBase):
    def __init__(self) -> None:
        ProductBase.__init__(self)
        ABC.__init__(self)
        # TODO: Maybe implement time.
        # self.created_at: datetime
        # self.last_modified_at: datetime
        # TODO: Maybe implement user.
        # self.writen_by: str = ""
        # self.last_modified_by: str = ""

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
