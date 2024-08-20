import os 
from time import sleep
os.system('clear')

# Инкапсуляция  🚨
# public         | общественный
# protect _      | защищать
# private __     | частный

class Teapot:
    def __init__(self, name, year, color) -> None:
        self.name = name
        self.year = year
        self.color = color
    
    def on(self):
        print(f"{self.name} is on")
        sleep(15)
        print(self.__heating())
        sleep(15)
        print(self.__boiling())
        sleep(2)
        return self._off()

    def _off(self):
        return f"{self.name} is off" 

    def __heating(self):
        return f"{self.name} is heating"
    
    def __boiling(self):
        return f"{self.name} is boiling"

    def __str__(self) -> str:
        return f"Teapot {self.name} - {self.year} {self.color}"
    

teapot1 = Teapot("LG", 2023, "red")
teapot2 = Teapot("Termax", 2022, "blue")
teapot3 = Teapot("Samsung", 2021, "black")

print(teapot1.on())
# print(teapot1._off())
# print(teapot1.__heating())
