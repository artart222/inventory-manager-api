from psycopg_pool import ConnectionPool

# For loading database settings from .env file.
import os
from dotenv import load_dotenv

from product import Product


class DataBase:
    def __init__(self) -> None:
        # Load the .env file
        load_dotenv()
        # Connect to the inventory database
        self.db_connection_pool = ConnectionPool(
            f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')} host={os.getenv('DB_HOST')}"
        )
        self.__init_table()

    def add_product(self, name, description, price, quantity, product_id=None):
        try:
            with self.db_connection_pool.connection() as conn, conn.cursor() as cursor:
                # TODO: There should be better way to put these values
                # in correct order. ths is just by order, I should do something
                # to do thing like this VALUES(product_id=id, ...)
                cursor.execute(
                    "INSERT INTO product (name, description, price, quantity) VALUES(%s,%s,%s, %s) RETURNING *",
                    (name, description, price, quantity),
                )

                conn.commit()
                print("Product added successfully!")
        except Exception as e:
            print(f"Error in adding product: {e}")
            conn.rollback()

    def get_product(self, product_id=None, name=None):
        if (product_id is None) and (name is None):
            print("Nothing was given for getting product")
            return Product()
        else:
            with self.db_connection_pool.connection() as conn, conn.cursor() as cursor:
                try:
                    # TODO: Can I do something like this?:
                    #  product_id or name = %s, (product_id or name)
                    if product_id:
                        cursor.execute(
                            "SELECT * FROM product WHERE product_id = %s", (product_id,)
                        )
                    elif name:
                        cursor.execute("SELECT * FROM product WHERE name = %s", (name,))
                    product = cursor.fetchone()
                    colnames = [desc[0] for desc in cursor.description]
                    row_dict = dict(zip(colnames, product))
                    return Product(**row_dict)
                except Exception as e:
                    print(f"Error retrieving product: {e}")
                    return None

    def delete_product(self, product_id=None, name=None):
        if (product_id is None) and (name is None):
            print("Nothing was given for deleting product")
            return None
        else:
            with self.db_connection_pool.connection() as conn, conn.cursor() as cursor:
                try:
                    if product_id:
                        cursor.execute(
                            "DELETE FROM product WHERE product_id = %s RETURNING *",
                            (product_id,),
                        )
                    elif name:
                        cursor.execute(
                            "DELETE FROM product WHERE name = %s RETURNING *", (name,)
                        )
                    deleted = cursor.fetchone()
                    conn.commit()
                    print("Product deleted successfully!")
                    return deleted
                except Exception as e:
                    print(f"Error in deleting product: {e}")
                    conn.rollback()

    def list_products(self):
        # I know this approach is not memory and cpu efficient
        # But it's good for small databases (around ten thousands)
        # And it will not keep connection pool open without any reason.
        with self.db_connection_pool.connection() as conn, conn.cursor() as cursor:
            try:
                cursor.execute("SELECT * FROM product")
                products = cursor.fetchall()
                products_list = []
                for product in products:  # iterator, fetches rows one by one
                    colnames = [desc[0] for desc in cursor.description]
                    row_dict = dict(zip(colnames, product))
                    products_list.append(Product(**row_dict))
                print("Product listed successfully!")
                return products_list
            except Exception as e:
                print(f"Error in listing products: {e}")
                conn.rollback()

    def update_product(self, args: dict, product_id=None, name=None):
        if not args or (product_id is None and name is None):
            print("Nothing was given for updating product")
            return None

        with self.db_connection_pool.connection() as conn, conn.cursor() as cursor:
            try:
                fields = ", ".join(f"{k} = %s" for k in args.keys())
                values = list(args.values())

                if product_id is not None:
                    query = (
                        f"UPDATE product SET {fields} WHERE product_id = %s RETURNING *"
                    )
                    values.append(product_id)
                else:
                    query = f"UPDATE product SET {fields} WHERE name = %s RETURNING *"
                    values.append(name)

                cursor.execute(query, values)
                updated_row = cursor.fetchone()
                conn.commit()
                print("Product updated successfully")
                return updated_row
            except Exception as e:
                print(f"Error in updating product: {e}")
                conn.rollback()
                return None

    def __init_table(self):
        with self.db_connection_pool.connection() as conn, conn.cursor() as cursor:
            try:
                # Using CREATE TABLE IF NOT EXISTS
                # to make product table if table doesn't exist and avoid the error.
                # TODO: Complete this.
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS product (
                    product_id BIGSERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    description TEXT,
                    price NUMERIC(10, 2),
                    quantity INT)
                """)
                conn.commit()
                print("Table created successfully")
            except Exception as e:
                print(f"Error in creating table: {e}")
                raise RuntimeError(f"Error in creating table: {e}")

    def close_connection(self):
        self.db_connection_pool.close()

    def __del__(self):
        self.db_connection_pool.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()
