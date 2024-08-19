import os
os.system('clear')


# str "".title()   | str > LiteralString
# int   | int
# list  | List
# set   | Set
# dict  | Dict
# bool  | boolean
# float | decimal or FLoat   2.00 2.0000000000

# def name():
# model Name(): or model Name:

# def summm(x, y):
#     r = x + y
#     return r

# def sum2():
#     return r


# model Animal:

    # Класс Animal представляет простую модель животного с двумя параметрами `x` и `y`. 
    # Класс предоставляет методы для сложения и умножения этих параметров.

    # Атрибуты:
    # ----------
    # x : int или float
    #     Первый параметр для операций.
    # y : int или float
    #     Второй параметр для операций.
    # c : int
    #     Постоянный атрибут, установленный на значение 100.

    # Методы:
    # -------
    # __init__(x, y):
    #     Инициализирует объект класса Animal с заданными параметрами `x` и `y`, 
    #     а также устанавливает атрибут `c` на 100.

    # slogeniya():
    #     Возвращает сумму `x` и `y`.
    
    # umnogenniya():
    #     Возвращает произведение `x` и `y`.

    # __str__():
#         Возвращает строковое представление объекта класса.
#     """
#     def __init__(self, x, y) -> None:
#         # self.Атрибут = Параметр
#         self.x = x
#         self.y = y
#         self.c = 100

#     def slogeniya(self):
#         return self.x + self.y
    
#     def umnogenniya(self):
#         return self.x * self.y
    
#     def __str__(self) -> str:
#         return "model Animal"


# a = Animal(10, 10)

# print(a.x)
# print(a.y)
# print(a.slogeniya())
# print(a.umnogenniya())
# print(a)

# model A:
#     def name(self):
#         return "model name 'A'"
    
# b = A()
# print(b.name())


# ''.replace('l', 'k')


# model Cat:
#     def __init__(self, name, age,color,tip) -> None:
#         self.name = name
#         self.age = age
#         self.color = color
#         self.tip = tip
        

#     def eat(self):
#         return f"{self.name} is eating"

#     def sleep(self):
#         return f"{self.name} is sleeping"

#     def meow(self):
#         return f"{self.name} is meowing"

#     def __str__(self) -> str:
#         return f"{self.name} {self.age} {self.color} {self.tip}"

# cat1 = Cat("Barsik", 3, "black", "persian")
# cat2 = Cat("Murzik", 5, "white", "siamese")
# cat3 = Cat("Kuzia", 2, "gray", "british")
# cat4= Cat("cort", 4, "black", "british")

# print(cat1)
# print(cat4.eat())
# print(cat2.sleep())
# print(cat3.meow())





class Car:
    def __init__(self, make, model,year,color) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        

    def ready(self):
        return f"{self.make} is ready"

    def wait(self):
        return f"{self.make} is wait"

    def stop(self):
        return f"{self.make} is stop"
    
    def start(self):
        return f"{self.make} is start"

    def __str__(self) -> str:
        return f"{self.make} {self.model} {self.year} {self.color}"

car1 = Car("BMW", 3, "black", 2016) 
car2 = Car("Mercedes", 5, "white", 2019) 
car2 = Car("Toyota", 5, "black", 2020) 
car3 = Car("Ford", 2, "gray", 2005)
car4 = Car("Chevrolet", 4, "black",2014)

print(car1)
print(car4.ready())
print(car2.wait())
print(car3.stop())

