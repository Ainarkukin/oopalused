class Koer():
    hyydnimi = ""
    vanus = 0
    #konstruktor
    def __init__(self, h, v):
        self.hyydnimi = h
        self.vanus = v
        self.saba = True

    def kirjeldus(self):
        print("Koer nimega " + self.hyydnimi + " on " + str(self.vanus) + " aastat vanus")

