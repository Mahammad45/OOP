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
# class Name(): or class Name:

# def summm(x, y):
#     r = x + y
#     return r

# def sum2():
#     return r


class Animal:
    """
    Класс Animal представляет простую модель животного с двумя параметрами `x` и `y`. 
    Класс предоставляет методы для сложения и умножения этих параметров.

    Атрибуты:
    ----------
    x : int или float
        Первый параметр для операций.
    y : int или float
        Второй параметр для операций.
    c : int
        Постоянный атрибут, установленный на значение 100.

    Методы:
    -------
    __init__(x, y):
        Инициализирует объект класса Animal с заданными параметрами `x` и `y`, 
        а также устанавливает атрибут `c` на 100.

    slogeniya():
        Возвращает сумму `x` и `y`.
    
    umnogenniya():
        Возвращает произведение `x` и `y`.

    __str__():
        Возвращает строковое представление объекта класса.
    """
    def __init__(self, x, y) -> None:
        # self.Атрибут = Параметр
        self.x = x
        self.y = y
        self.c = 100

    def slogeniya(self):
        return self.x + self.y
    
    def umnogenniya(self):
        return self.x * self.y
    
    def __str__(self) -> str:
        return "Class Animal"


a = Animal(10, 10)

# print(a.x)
# print(a.y)
# print(a.slogeniya())
# print(a.umnogenniya())
# print(a)

# class A:
#     def name(self):
#         return "class name 'A'"
    
# b = A()
# print(b.name())


# ''.replace('l', 'k')


class Cat:
    def __init__(self, name, age,color,paroda) -> None:
        self.name = name
        self.age = age
        self.color = color
        self.paroda = paroda
        

def eat(self):
    return f"{self.name} is eating"

def sleep(self):
    return f"{self.name} is sleeping"

def meow(self):
    return f"{self.name} is meowing"

def __str__(self) -> str:
    return f"{self.name} {self.age} {self.color} {self.paroda}"