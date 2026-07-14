class Subor():
    def __init__(self, meno_suboru):
        self.meno_suboru = meno_suboru
        open(self.meno_suboru, 'w').close()
    def pripis(self,text):
        open(self.text, 'a').close()
    def vypis(self):
        return 







s = Subor('text.txt')
s.pripis('prvy riadok')
s.pripis('druhy riadok')
s.vypis()
s.pripis('posledny riadok')
print('***')
s.vypis()