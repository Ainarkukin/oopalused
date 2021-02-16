class Auto():
    def __init__(self, t, m, a):
        self.tootja = t
        self.mudel = m
        self.aasta = a
        self.odomeeteri_nait = 0

    def kirjeldus(self):
        pikk_nimi = str(self.aasta) + " " + self.tootja + self.mudel
        return pikk_nimi.title()

    def odomeeter(self):
        print("Antud auto sõitnud läbi " + str(self.odomeeteri_nait) + "km.")