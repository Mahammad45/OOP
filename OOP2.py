import os 
from time import sleep
os.system('clear')

# Инкапсуляция  🚨
# public         | общественный
# protect _      | защищать
# private __     | частный

class Teapot:
    def __init__(self, owner, year, color) -> None:
        self.owner = owner
        self.year = year
        self.color = color
    
    def on(self):
        print(f"{self.owner} is on")
        sleep(15)
        print(self.__heating())
        sleep(15)
        print(self.__boiling())
        sleep(2)
        return self._off()

    def _off(self):
        return f"{self.owner} is off" 

    def __heating(self):
        return f"{self.owner} is heating"
    
    def __boiling(self):
        return f"{self.owner} is boiling"

    def __str__(self) -> str:
        return f"Teapot {self.owner} - {self.year} {self.color}"
    

teapot1 = Teapot("LG", 2023, "red")
teapot2 = Teapot("Termax", 2022, "blue")
teapot3 = Teapot("Samsung", 2021, "black")

# print(teapot1.on())
# print(teapot1._off())
# print(teapot1.__heating())



class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance__ = balance

    def deposit(self, amount):
        """Метод для пополнения счета."""
        if amount > 0:
            self.__balance__+= amount
            print(f"{amount} has been deposited. New balance is {self.__balance__}")
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.__balance__:
            print("Insufficient funds")
        else:
            self.__balance__ -= amount
            print(f"{amount} has been withdrawn. New balance is {self.__balance__}")

    def __str__(self):
        return f"Account of {self.owner} with balance {self.__balance__}"
