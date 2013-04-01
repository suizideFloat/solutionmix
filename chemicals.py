
# coding: utf8

class GenericChemical(object):

    def __init__(self, mass, structur, dense, physcon):
        #self.name = __init__.name
        self.mass = mass
        self.structur = structur
        self.dense = dense
        self.physcon = physcon

    def temp_to_loesen(self):
        raise NotImplementedError(
            'Methode temp_to_loesen nicht implementiert.'
            )


class NatriumChlorid(GenericChemical):
    def __init__(self):
        GenericChemical.__init__(self, 58.44, 'NaCl', 2.17, 'solid')
    # def GenericChemical.__init__(self, 58.44, 'NaCl', 2.17, 'solid'):

    def dummy_func(self):
        return None


class Salzsaeure(GenericChemical):

    def __init__(self):
        GenericChemical.__init__(self,36.46, 'HCl', 1.64, 'gaseous')

    def dummy_func(self):
        return None