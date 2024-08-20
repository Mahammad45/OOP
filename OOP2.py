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
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        """Метод для пополнения счета."""

        if amount > 0:
            self.__balance += amount
            return f"{amount} был добавлен на ваш счет. Теперь ваш баланс составляет {self.__balance}"
        
        else:
            return "Сумма депозита не должна быть нулем или меньше."

    def withdraw(self, amount):
        """Метод для снятия денег со счета."""

        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                return f"{amount} был снят с вашего счета. Теперь ваш баланс составляет {self.__balance}"
            else:
                return "Недостаточно средств на счету."
        else:
            return "Сумма снятия не должна быть нулем или меньше."


account1 = BankAccount('Marselle', 100)

print(account1.deposit(500))
print(account1.withdraw(300))

