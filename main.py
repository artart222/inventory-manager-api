from product import Product
from db import DataBase

a = Product()
a.set_product_details(
    product_id=2411323,
    name="Car",
    description="My beatiful car",
    price=32000,
    quantity=15,
)
print(
    a.get_product_details().get("product_id"),
    a.get_product_details().get("name"),
    a.get_product_details().get("description"),
    a.get_product_details().get("price"),
    a.get_product_details().get("quantity"),
)


# d=DataBase.connect_to_db()
d = DataBase()
print(
    d.add_product(
        a.get_product_details().get("product_id"),
        a.get_product_details().get("name"),
        a.get_product_details().get("description"),
        a.get_product_details().get("price"),
        a.get_product_details().get("quantity"),
    )
)
print(d.get_product(product_id=2411323))
del d
# d.read_config("db.ini", "postgresql")
