class Andmed:
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]


class Opetaja:
    def opetab(self, info, opilane):
        for i in opilane:
            i.opib(info)

class opilane
    def __init__(self):
        self.teadmised = []
    def opib(self, info):
        self.teadmised.append(info)