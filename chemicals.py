
# coding: utf8

class GenericChemical(object):
    def __init__(self, mass, structur, dense, physcon):
        self.name = __init__.name
        self.mass = None
        self.structur = None
        self.dense = None
        self.physcon = None

class NatriumChlorid(GenericChemical):
    def __init__(self, mass, structur, dense, physcon):
        GenericChemical.__init__(self, 58.44, 'NaCl', 2.17, 'solid') # Wichtige Zeile - siehe unten
    # def GenericChemical.__init__(self, 58.44, 'NaCl', 2.17, 'solid'):
        self.mass = mass
        self.structur = structur
        self.dense = dense
        self.physcon = physcon


class Salzsure(GenericChemical):

    def __init__(self, mass, structur, dense, physcon):
        GenericChemical.__init__(self)
    # 36.46, 'HCl', 1.64, 'gaseous'

        self.mass = mass
        self.structur = structur
        self.dense = dense
        self.physcon = physcon