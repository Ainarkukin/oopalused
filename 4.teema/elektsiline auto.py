from auto import Auto
class ElektriAuto(Auto):
    def __init__(self, t, m, a):
        Auto().__init__(t,m,a)
        self.akuSuurus = 50

    def akuKirjeldus(self):
        print("Antud auto sisaldab " + str(self.akuSuurus) + " patarei")