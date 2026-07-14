#інкапсуляція
class Animal(): #базовий клас
    def __init__(self,name, age):
        self._name=name
        self._age=age

    def speek(self):
        return f"{self._name} нічого не каже..."

    def info(self):
        return f"{self._name} {self._age} років"

class Dog(Animal): #створяється на основі базового
    def speek(self):
        return f"{self._name} каже ГАВ" #поліморфізм
class Cat(Animal): #створяється на основі базового
    def speek(self):
        return f"{self._name} каже МЯУ" #поліморфізм

animals=[
    Cat("Барсик", 5),
    Cat("Мурчик", 9),
    Dog("Сірко", 7),
    Dog("Рекс", 8)
]
for animal in animals:
    print(animal.info())

for animal in animals:
    print(animal.speek())