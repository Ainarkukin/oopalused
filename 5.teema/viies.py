class Ristkülik:
    def __init__(self, laius, korgus, symbol):
        self.width = int(laius)
        self.height = int(korgus)
        self.symbol = str(symbol)

    def __str__(self):
        ruut = []
        for i in range(self.height):
            ruut.append(self.symbol * self.width)
        ruut = '\n'.join(ruut)
        return ruut

    def __add__(self, x):
        self.width = self.width + x.width
        self.height = self.height + x.height
        self.symbol = self.symbol


kujund1 = Ristkülik(10, 3, '*')
print(kujund1)
kujund2 = Ristkülik(8, 3, 'z')
print(kujund2)

kujund1.__add__(kujund2)
print(kujund1)
