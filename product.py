from abc import ABC
from datetime import datetime


class ProductBase:
    def __init__(self) -> None:
        self.name: str = ""
        self.id: str | int = ""
        self.description: str = ""
        self.price: float = 0.0
        self.quantity: int = 0


class Product(ABC, ProductBase):
    def __init__(self) -> None:
        ProductBase.__init__(self)
        ABC.__init__(self)
        self.created_at: datetime
        self.last_modified_at: datetime
        self.writen_by: str = ""
        self.last_modified_by: str = ""
