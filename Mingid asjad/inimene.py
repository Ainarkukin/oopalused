class Inimene:
    def __init__(self, eesnimi, perenimi, kutsekvalifikatsioon, parool = "QWERTY"):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
        self.kutsekvalifikatsioon = kutsekvalifikatsioon
        self.sisselogimiskatsed = 0
        self.__parool = parool
        global miinimumlist
        miinimumlist = []

    def maara_parool(self, x):
        self.__parool = x
        print("Parool on määratud!")
        print("AKN ")

    def naita_parool(self):
        print(self.eesnimi + " parool on hetkel " + self.__parool)

    def kasutajanimi(self):
        print(self.eesnimi.lower() + "." + self.perenimi.lower())
    def parool(self):
        self.naita_parool()

    def kontrolli_parool(self, x):
        if len(x) >= 6 and len(x) <= 10:
            self.maara_parool(x)
            print("Parooli muutmine on õnnestunud!")
        elif len(x) < 8:
            print("Parooli muutmine on ebaõnnestunud")
            print("Parool liiga lühike, peab olema vähemalt 8 tähte ja symbolid")
        elif len(x) > 9:
            print("Parooli muutmine ebaõnnestunud")
            print("Parool liiga pikk, peab olema vähem kui 9 tähte ja symbolid")

    def getmin(self):
        miinimum = self.kutsekvalifikatsioon
        miinimumlist.append(miinimum)

    def suurenda_sisselogimiskatsed(self):
        self.sisselogimiskatsed += 1
        print("Kasutaja " + str(self.eesnimi), str(self.perenimi) + " on hetkel seisuga olete loginud  " + str(self.sisselogimiskatsed) + " korda")

    def reset_sisselogimiskatsed(self):
        self.sisselogimiskatsed = 0
        print("resetitud sisselogimiskatsed kasutajal " + str(self.eesnimi), str(self.perenimi) + " ja nüüd on " + str(self.sisselogimiskatsed) + " korda sisse logitud")

    def __del__(self):
        if self.kutsekvalifikatsioon == min(miinimumlist):
            print(str(self.eesnimi) + " " + str(self.perenimi) + " Teil ei ole piisavalt hea kutsekvalifikatsioon!")
        else:
            print("Liigume edasi")

    def tutvustus(self):
        print("Tere! Olen " + self.eesnimi + " " + self.perenimi + ". Mu kasutajanimi on " + self.eesnimi.lower() + "." + self.perenimi.lower() + " ja parool on " + self.__parool)