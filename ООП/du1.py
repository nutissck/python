class Zlomok():
    def __init__(self, citatel, menovatel):
        self.citatel = citatel
        self.menovatel = menovatel
    def vypis(self):
        print(f"zlomok je {str(self.citatel)}/{self.menovatel}")
    def str(self):
        return f"{self.citatel}/{self.menovatel}"
    def float(self):
        return round(self.citatel/self.menovatel, 2)

z1 = Zlomok(3, 8)
z2 = Zlomok(2, 4)

z1.vypis()
z2.vypis()

z = Zlomok(3, 8)
print('z je', z.str())
print('z je', z.float())
w = Zlomok(2, 4)
print('w je', w.str())
print('w je', w.float())