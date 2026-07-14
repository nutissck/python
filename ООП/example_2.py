#наслідування(успадкування)
class Animal(): #базовий клас
    def __init__(self,name):
        self.name=name
        self.fed=False

    def eat(self, food):
        print(self.name, "eat", food)
        self.fed=True

class Dog(Animal): #створяється на основі базового
    def guard(self):
        if not self.fed:
            print(self.name, "охраняє")
        else:
            print(self.name, "спить")
class Cat(Animal): #створяється на основі базового
    def catchvouse(self):
        if self.fed:
            print(self.name, "спить")
        else:
            print(self.name, "ловить мишу")

cat1=Cat("Luna")
cat1.eat("fish")
cat1.catchvouse()

dog1=Dog("Tom")
dog1.eat("meat")
dog1.guard()

