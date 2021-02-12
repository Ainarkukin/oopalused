class Kasutajad():
    kasutaja_nimi = ""
    def __init__(self, e, p):
        self.eesnimi = e
        self.perenimi = p
    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi " + (self.eesnimi))
        print("Kasutaja perekonnanimi on " + (self.perenimi))
    def maara_kasutaja_nimi(self, k):
        self.kasutaja_nimi = k