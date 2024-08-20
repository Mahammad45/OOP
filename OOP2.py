import os
import sys

os.sysyem('clear')

# Инкапсуляция
# public
# protect _
# private __


class Tefal:
    def __init__(self,name,year,color) -> None:
        self.name = name
        self._year = year
        self.__color = color

    