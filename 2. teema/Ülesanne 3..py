from Kasutajad import Kasutajad
alice = Kasutajad()
alice.eesnimi = "Alice"
alice.perenimi = "Ime"
alice.kasutaja_nimi = "Alice"
alice.parool = "QWERTY"
alice.kirjelda_kasutaja()
print()
alice.tervita_kasutaja()

kaspar = Kasutajad()
kaspar.eesnimi = "Kaspar"
kaspar.perenimi = "Ilus"
kaspar.kasutaja_nimi = "Kaspar"
kaspar.parool = "QWERTY"
kaspar.kirjelda_kasutaja()
print()
kaspar.tervita_kasutaja()

meelis = Kasutajad()
meelis.eesnimi = "Meelis"
meelis.perenimi = "Mesine"
meelis.kasutaja_nimi = "Kaspar"
meelis.parool = "QWERTY"
meelis.kirjelda_kasutaja()
print()
meelis.tervita_kasutaja()

