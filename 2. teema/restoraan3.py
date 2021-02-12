class Restoraan():
    def __init__(self, nimi, sook):
        self.restoraani_nimi = nimi
        self.soogi_tyyp = sook
    def restoraani_kirjeldus(self):
        print("Restoraan " + str(self.restoraani_nimi) + ", söögi tüüp " + str(self.soogi_tyyp))
    def ava_restoraan(self):
        print("Restoraan on avatud")
