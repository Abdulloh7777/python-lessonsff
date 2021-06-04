import sqlite3
from dao.productDAO import ProductDAO


class DBController:
    __dbname = "warehouse.db"


    def __init__(self) -> None:
        self.__connection = self.__initiate()
        self.__prodDAO = ProductDAO(self.__connection)

    
    def __initiate(self):
        return sqlite3.connect(self.__dbname)
    

    def call_process(self, user, product_list):
        if user.get_role() == "SALES":
            self.__prodDAO.outgo(product_list)
        elif user.get_role() == "WAREHOUSE":
            self.__prodDAO.income(product_list)

