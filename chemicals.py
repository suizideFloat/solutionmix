
# coding: utf8

class GenericChemical(object):

    def __init__(self, mass, structur, dense, physcon, max_conc):
        #self.name = __init__.name
        self.mass = mass
        self.structur = structur
        self.dense = dense
        self.physcon = physcon
        self.max_conc = max_conc

    def temp_to_loesen(self):
        raise NotImplementedError(
            'Methode temp_to_loesen nicht implementiert.'
            )



class Wasser(GenericChemical):
    def __init__(self):
        GenericChemical.__init__(self, 18.0153, 'H2O', 1.00, 'liquid', None)
    # def GenericChemical.__init__(self, 58.44, 'NaCl', 2.17, 'solid'):

    def dummy_func(self):
        return None


class Salzsaeure(GenericChemical):

    def __init__(self):
        GenericChemical.__init__(self, 36.46, 'HCl', 1.64, 'gaseous', 37)

    def dummy_func(self):
        return None


class Schwefelsaeure(GenericChemical):

    def __init__(self):
        GenericChemical.__init__(self, 98.08, 'H2SO4', 1.8356, 'liquid', 98)


class Salpetersaeure(GenericChemical):

    def __init__(self):
        GenericChemical.__init__(self, 63.01, 'HNO3', 1.51, 'liquid', 65)

    def dummy_func(self):
        return None
