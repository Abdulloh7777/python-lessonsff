from core.dbController import DBController
from objects.product import Product
from objects.user import User
import os


controller = DBController()
teshavoy = User("tesha2005", "qwerty", "SALES")
boltavoy = User("boltavoy", "qwerty", "WAREHOUSE")


while True:
    print("""
    MARKET MANAGEMENT APP
    Iltimos, birinchi avtorizatsiyadan o'ting
    """)
    username = input("Username: ")
    password = input("Password: ")
    
    os.system("clear")
    product_list = list()
    if (boltavoy.check_username(username) and boltavoy.check_password(password)):
        while True:
            print("Yangi tovar kirimini registratsiya qilish uchun quyidagi ma'lumotlarni kiriting")
            name = input("Tovar: ")
            price = float(input("Narxi: "))
            amount = float(input("Miqdori: "))

            prod = Product(0, name, price, amount)
            product_list.append(prod)

            cmd = input("Yana tovar bormi? [H / Y]: ")
            if cmd == "Y":
                controller.call_process(boltavoy, product_list)
                product_list.clear()
                break
    
    elif (teshavoy.check_username(username) and teshavoy.check_password(password)):
        while True:
            print("Yangi tovar chiqimini registratsiya qilish uchun quyidagi ma'lumotlarni kiriting")
            name = input("Tovar: ")
            amount = float(input("Miqdori: "))

            prod = Product(0, name, 0, amount)
            product_list.append(prod)

            cmd = input("Yana tovar bormi? [H / Y]: ")
            if cmd == "Y":
                controller.call_process(teshavoy, product_list)
                product_list.clear()
                break
    else:
        print("Login yoki parol xato. Boshidan urinib ko'ring")
    
