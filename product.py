class Product:
    def __init__(self, id, name, price, amount) -> None:
        self.__id = id
        self.__name = name
        self.__price = price
        self.__amount = amount


    def get_id(self):
        return self.__id


    def get_name(self):
        return self.__name


    def get_price(self):
        return self.__price


    def get_amount(self):
        return self.__amount
    

    def increase(self, amount):
        self.__amount += amount


    def decrease(self, amount):
        if self.__amount < amount:
            return f"Not enough. {self.__name}: {self.__amount}"
        
        self.__amount -= amount
    

    def __str__(self):
        return f"{self.__name}"