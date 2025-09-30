from product import Product
from db import DataBase

a = Product()
a.set_product_details(
    name="Car",
    description="My beautiful car",
    price=32000,
    quantity=15,
)

b = Product(
    name="Cat",
    description="Out Inventory Cat",
    price=100,
    quantity=5
)
print(b.get_product_details())

a.set_product_details(quantity=10)
print(a.get_product_details())

d = DataBase()
d.add_product(**a.get_product_details())
d.add_product(**b.get_product_details())

for i in d.list_products():
    print(i.get_product_details())

print(type(d.get_product(d.list_products()[0].get_product_details().get("product_id"))))
print(d.update_product(product_id=d.list_products()[0].get_product_details().get("product_id"),args={"price":10}))
print(d.delete_product(d.list_products()[0].get_product_details().get("product_id")))
print(d.list_products()[0].get_product_details())

for i in d.list_products():
    print(i.get_product_details())