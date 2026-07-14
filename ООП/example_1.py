class Cat():
    def __init__(self,name,color, hungry):
        self.name=name
        self.color=color
        self.hungry=hungry    #конструктор класу
cat1=Cat("Tom","red",True)
cat2=Cat("Max","grey",False)
cat3=Cat("Fill", "black", True)
print(cat1.name)
print(cat2.name)
print(cat3.name)
