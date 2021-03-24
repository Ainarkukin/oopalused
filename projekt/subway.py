sailist = ["Valge sai", "Köömnetega sai", "Röst sai"]
lisandidlist = ["Jääsalat",  "Tomat", "Kurk","Sink", "Juust", "Punane sibul"]
maitselist = ["Sool", "Pipar"]
kastmelist = ["Ketšup", "Majonees", "Tšilli", "Kartuli kaste"]
joogidlist = ["Coca-cola",  "Vesi", "Jäätee", "Kohvi",  "Maitsevesi"]

class Subway():
    def __init__(self, nimi):
        self.nimi = nimi

    def Kysimused(self):
        print("Tere tulemast", self.nimi, "subway restorani. Palun valige milline on teie võileib välja näeb!")

    def sai(self):
        print("1. Valge sai 2. Köömnetega sai 3. Röst sai")
        sai = int(input("Palun sisestage valikutest, millist saia tüüpi te soovite!"))
        return sai

    def Lisandid(self):
        print("1. Jääsalat 2. Tomat 3. Kurk 4. Sink 5. Juust 6. Punane sibul")
        Lisandid = int(input("Palun sisestage valikutest, milliseid lisandeid te soovite!"))
        return Lisandid

    def maitseained(self):
        print("1. Sool 2. Pipar")
        maitseaine = int(input("Palun sisestage valikutest, millist maitseainet te soovite!"))
        return maitseaine

    def kastmed(self):
        print("1. Ketšup 2. Majonees 3. Tšilli 4. Kartuli kaste 5.")
        kastmed = int(input("Palun sisestage kastmed, kui on soovi!"))
        return kastmed

    def joogid(self):
        print("1. Coca-cola 2. Vesi 3. Jäätee 4. Kohvi 5. Maitsevesi")
        joogid = int(input("Palun sisestage valikutest, millist jooki/jooke te soovite!"))
        return joogid

    def Tulemus(self):
        print(sailist[self.sai()-1])
        print(lisandidlist[self.Lisandid()-1])
        print(maitselist[self.maitseained()-1])
        print(kastmelist[self.kastmed()-1])
        print(joogidlist[self.joogid() - 1])