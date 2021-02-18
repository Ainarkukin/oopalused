class Inimene():
    jk = 0
    def __init__(self):
        self.id = self.jk + 1
        self.jk += 1

    def info(self):
        print("Inimese id = " + str(self.id))
        print("Inimese jk = " +str(self.jk))
