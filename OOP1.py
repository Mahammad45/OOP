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
# brand Name(): or brand Name:

# def summm(x, y):
#     r = x + y
#     return r

# def sum2():
#     return r


# brand Animal:

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
#         return "brand Animal"


# a = Animal(10, 10)

# print(a.x)
# print(a.y)
# print(a.slogeniya())
# print(a.umnogenniya())
# print(a)

# brand A:
#     def name(self):
#         return "brand name 'A'"
    
# b = A()
# print(b.name())


# ''.replace('l', 'k')


# brand Cat:
#     def __init__(self, name, age,price,tip) -> None:
#         self.name = name
#         self.age = age
#         self.price = price
#         self.tip = tip
        

#     def eat(self):
#         return f"{self.name} is eating"

#     def sleep(self):
#         return f"{self.name} is sleeping"

#     def meow(self):
#         return f"{self.name} is meowing"

#     def __str__(self) -> str:
#         return f"{self.name} {self.age} {self.price} {self.tip}"

# cat1 = Cat("Barsik", 3, "black", "persian")
# cat2 = Cat("Murzik", 5, "white", "siamese")
# cat3 = Cat("Kuzia", 2, "gray", "british")
# cat4= Cat("cort", 4, "black", "british")

# print(cat1)
# print(cat4.eat())
# print(cat2.sleep())
# print(cat3.meow())





# class Car:
#     def __init__(self, name, brand,category,price) -> None:
#         self.name = name
#         self.brand = brand
#         self.category = category
#         self.price = price
        

#     def ready(self):
#         return f"{self.name} is ready"

#     def wait(self):
#         return f"{self.name} is wait"

#     def stop(self):
#         return f"{self.name} is stop"
    
#     def start(self):
#         return f"{self.name} is start"

#     def __str__(self) -> str:
#         return f"{self.name} {self.brand} {self.category} {self.price}"

# car1 = Car("BMW", 3, "black", 2016) 
# car2 = Car("Mercedes", 5, "white", 2019) 
# car2 = Car("Toyota", 5, "black", 2020) 
# car3 = Car("Ford", 2, "gray", 2005)
# car4 = Car("Chevrolet", 4, "black",2014)

# print(car1)
# print(car4.ready())
# print(car2.wait())
# print(car3.stop())




class Product:
    def __init__(self, name, brand,category,price,description,calories,fat,carbohydrates,protein,fiber) -> None:
        self.name = name
        self.brand = brand
        self.category = category
        self.price = price
        self.description = description
        self.calories = calories
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein
        self.fiber = fiber

        

    def ready(self):
        return f"{self.name} is old"

    def wait(self):
        return f"{self.name} is new"

    def stop(self):
        return f"{self.name} is finish"
    
    def start(self):
        return f"{self.name} is last 1"

    def __str__(self) -> str:
        return f"{self.name} {self.brand} {self.category} {self.price} {self.description} {self.calories}{self.fat} {self.carbohydrates} {self.protein} {self.fiber}"

 
product1 = Product("Milk", "MilkCompany", "milk", 2.5, "milk for human", 100, 3, 5, 2, 0)
product2 = Product("Bread", "BreadCompany", "bread", 1.5, "bread for human", 150, 2, 10, 3, 1)
product3 = Product("Eggs", "EggsCompany", "eggs", 3.0, "eggs for human", 200, 4, 8, 6, 0)
product4 = Product("Cheese", "CheeseCompany", "cheese", 4.0, "cheese for human", 250, 6, 4, 8, 2)
product5 = Product("Butter", "ButterCompany", "butter", 5.0, "butter for human", 300, 8, 2, 10, 0)


print(product1)
print(product4.ready())
print(product2.wait())
print(product3.stop())


