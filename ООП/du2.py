class Body():
    def __init__(self):
        self.bod = 0
    def pridaj(self):
        self.bod += 1
    def uber(self):
        self.bod -= 1
    def kolko(self):
        return self.bod
b = Body()
for i in range(10):
    b.pridaj()
b.uber()
b.uber()
print('body =', b.kolko())
