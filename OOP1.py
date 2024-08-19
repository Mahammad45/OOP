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
