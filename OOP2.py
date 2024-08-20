import os
import sys

os.sysyem('clear')

# Инкапсуляция
# public      | общественный
# protect _    | защищать
# private __    | частный


class Teapot:
    def __init__(self,name,year,color) -> None:
        self.name = name
        self._year = year
        self.__color = color

    def on(self):
        return(f'{self.name} is on')
    def off(self):
        return(f'{self.name} is off')
    
    def heating(self):
        return(f'{self.name} is heating')
    
    def __str__(self) -> str:
        return(f'{self.name} {self._year} {self.__color}')
    

    Teapot = Teapot('LG', 2020, 'black')
    Teapot1= Teapot('BEKO', 2019, 'white')
    Teapot2= Teapot('SAMSUNG', 2018, 'red')
    Teapot3= Teapot('TERMAX', 2017, 'blue')
    Teapot4= Teapot('Teapot', 2016, 'green')