import psycopg
import os

from dotenv import load_dotenv


class DataBase:
    def __init__(self) -> None:
        # Load the .env file
        load_dotenv()

        # Connect to the inventory database
        self.db_connection = psycopg.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password="az2685%64578",
            host=os.getenv("DB_HOST"),
        )
        print(self.db_connection)

    def add_product(self, product_id, name, desciption, price, quantity):
        try:
            with self.db_connection.cursor() as cursor:
                # Use IF NOT EXISTS to avoid the error
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS product (
                    product_id BIGINT PRIMARY KEY,
                    name VARCHAR(20),
                    description TEXT,
                    price NUMERIC(10, 2),
                    quantity INT)
                """)
                print(product_id, name, desciption, price, quantity)
                cursor.execute(
                    "INSERT INTO product VALUES(%s,%s,%s, %s, %s)",
                    (product_id, name, desciption, price, quantity),
                )

                self.db_connection.commit()
                print("Product added successfully!")

        except Exception as e:
            print(f"Error: {e}")
            self.db_connection.rollback()

    def get_product(self, product_id=None, name=None):
        if (product_id is None) and (name is None):
            print("Nothing was given for getting product")

        if (product_id is not None) and (name is None):
            try:
                with self.db_connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM product WHERE product_id = %s", (product_id,)
                    )
                    product = cursor.fetchone()
                    return product
            except Exception as e:
                print(f"Error retrieving product: {e}")
                return None
        elif (name is not None) and (product_id is None):
            try:
                with self.db_connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM product WHERE product_id = %s", (product_id,)
                    )
                    product = cursor.fetchone()
                    return product
            except Exception as e:
                print(f"Error retrieving product: {e}")
                return None
        else:
            print("Why you damn fool give me all this data")

    def __del__(self):
        self.db_connection.close()
