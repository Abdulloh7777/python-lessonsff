from objects.product import Product

class ProductDAO:
    def __init__(self, connection) -> None:
        self.__connection = connection
        self.__dbcreate()
        self.__products = list()
    

    def __dbcreate(self):
        create = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name VARCHAR(32) UNIQUE,
            price REAL,
            amount REAL
        )
        """

        self.__connection.execute(create)
    

    def income(self, product_list):
        self.__collect_data()

        if len(self.__products) > 0:
            for item in product_list:
                prod = self.__check_similarity(item)
                if prod == None:
                    prod = item
                else:
                    prod.increase(item.get_amount())
                
                self.__products.append(prod)
        else:
            self.__products = product_list
        
        self.__commit_data()


    def outgo(self, product_list):
        self.__collect_data()

        if len(self.__products) > 0:
            for item in product_list:
                prod = self.__check_similarity(item)
                prod.decrease(item.get_amount())
                self.__products.append(prod)
        else:
            self.__products.clear()
            return
        
        self.__commit_data()


    def __check_similarity(self, product):
        for index in range(len(self.__products)):
            if self.__products[index].get_name() == product.get_name():
                return self.__products.pop(index)
            else:
                return None


    def __collect_data(self) -> list:
        select = """
        SELECT * FROM products
        """
        cursor = self.__connection.execute(select)
        for item in cursor.fetchall():
            prod = Product(item[0], item[1], item[2], item[3])
            self.__products.append(prod)
    

    def __commit_data(self):
        for product in self.__products:
            if product.get_id() > 0:
                insert = f"""
                UPDATE products
                SET amount = {product.get_amount()}, price = {product.get_price()}
                WHERE id = {product.get_id()}
                """
            else:
                insert = f"""
                INSERT INTO products (name, amount, price)
                VALUES ('{product.get_name()}', {product.get_amount()}, {product.get_price()})
                """
            
            self.__connection.execute(insert)
        
        self.__connection.commit()
        self.__products.clear()
