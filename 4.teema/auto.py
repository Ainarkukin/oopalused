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

    def uuenda_odomeetr(self, km):
        if km >= self.odomeeteri_nait = km
        self.odomeeteri_nait = km
        else:
            print("Ei ole võimalik tagasi keerata odomeetri näit")

    def suurenda_odomeeter(self, km):
        self.odomeeteri_nait += km