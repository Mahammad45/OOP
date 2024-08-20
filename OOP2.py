import os 
from time import sleep
os.system('clear')

# Инкапсуляция  🚨
# public         | общественный
# protect _      | защищать
# private __     | частный

class Teapot:
    def __init__(self, owner, __is_checked_out, color) -> None:
        self.owner = owner
        self.__is_checked_out = __is_checked_out
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
        return f"Teapot {self.owner} - {self.__is_checked_out} {self.color}"
    

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

    def get_balance(self):
        """Метод для получения текущего баланса."""

        return f"Ваш Баланс составлает {self.__balance}"
    
    def __apply_fees(self):
        """Приватный метод для применения комиссии."""
        fees = self.__balance *0.1
        self.__balance -= fees
        return f"Комиссия {fees} была снята с вашего счета."
    

    def month_end(self):
        """Метод для обработки месячного окончания счета."""
        self.__apply_fees()
        return f"Ваш счет был обработан. Теперь ваш баланс составляет {self.__balance}"

    def __str__(self) -> str:
        return f"BankAccount {self.owner} - {self.__balance}"

account1 = BankAccount('Marselle', 100)

# print(account1.deposit(500))
# print(account1.withdraw(300))
# print(account1.get_balance())
# print(account1.month_end())




class LibraryBook:
    def __init__(self, title, author, __is_checked_out) -> None:
        self.title = title
        self.author = author
        self.__is_checked_out = __is_checked_out
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."

    def status(self):
        if self.is_checked_out:
            return f"{self.title} is checked out."
        else:
            return f"{self.title} is available."
    
    def calculate_fine(self, days_late):
        return days_late * 0.5
    def return_with_fine(self, days_late):
        fine = self.calculate_fine(days_late)
        self.is_checked_out = False
        return f"{self.title} has been returned. Fine: ${fine}"
    
    def enew(self):
        return f"{self.title} has been renewed."
    def return_with_fine(self, days_late):
        fine = self.calculate_fine(days_late)
        self.is_checked_out = False
        return f"{self.title} has been returned. Fine: ${fine}"

    def __str__(self) -> str:
        return f"LibraryBook {self.title} by {self.author} ({self.__is_checked_out})"
    
    


book=LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", False)