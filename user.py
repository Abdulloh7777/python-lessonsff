class User:
    def __init__(self, username, password, role) -> None:
        self.__username = username
        self.__password = password
        self.__role = role


    def get_role(self):
        return self.__role
    

    def check_username(self, usrnme):
        return True if self.__username == usrnme else False
    

    def check_password(self, pswd):
        return True if self.__password == pswd else False


    def __str__(self):
        return f"{self.__username} - {self.__role}"