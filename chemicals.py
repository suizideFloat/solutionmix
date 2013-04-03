
# coding: utf8

class GenericChemical(object):

    def __init__(self, mass, structur, dense, physcond, max_conc, temp, sec_code):
        #self.name = __init__.name
        self.mass = mass
        self.structur = structur
        self.dense = dense
        self.physcond = physcond
        self.max_conc = max_conc
        self.temp = temp
        self.sec_code = sec_code

    def temp_to_loesen(self):
        raise NotImplementedError(
            'Methode temp_to_loesen nicht implementiert.'
            )



class Wasser(GenericChemical):

    def __init__(self):
        GenericChemical.__init__(self, 18.0153, 'H2O', 1.00, 'liquid', None, None, None)
    # def GenericChemical.__init__(self, 58.44, 'NaCl', 2.17, 'solid'):

    def heating(self, wert):
        self.temp = wert
        #return self.temp

    def change_physcond(self,newcond):
        if self.temp < 0:
            self.physcond = 'solid'
        #return self.physcond

    def ch_dense(self):
        if self.temp >= 20:
            newdense = 0.998203
            self.dense = newdense
        return self.dense

class Salzsaeure(GenericChemical):

    def __init__(self):
        GenericChemical.__init__(self, 36.46, 'HCl(aq)', 1.19, 'liquid', 37, None, ['caustic'])


class Schwefelsaeure(GenericChemical):

    def __init__(self):
        GenericChemical.__init__(self, 98.08, 'H2SO4', 1.8356, 'liquid', 98, None, ['caustic'])


class Salpetersaeure(GenericChemical):

    def __init__(self):
        GenericChemical.__init__(self, 63.01, 'HNO3', 1.51, 'liquid', 65, None, ['caustic','oxidizing'])


class Wasserstoffperoxid(GenericChemical):

    def __init__(self):
        GenericChemical.__init__(self, 34.02, 'H2O2', 1.47, 'liquid', 100, None, ['caustic','oxidizing'])


class Ethanol(GenericChemical):

    def __init__(self):
        GenericChemical.__init__(self, 46.07, 'C2H6O', 0.79, 'liquid', 96, None, ['highly flammable'])


class Isopropanol(GenericChemical):

    def __init__(self):
        GenericChemical.__init__(self, 60.10, 'C3H8O', 0.78, 'liquid', 99.9, None, ['highly flammable', 'irritant'])


class Methanol(GenericChemical):

    def __init__(self):
        GenericChemical.__init__(self, 32.04, 'CH4O', 0.79, 'liquid', 99.98, None, ['highly flammable', 'toxic'])


class Phosphorsaeure(GenericChemical):

    def __init__(self):
        GenericChemical.__init__(self, 98.00, 'H3PO4', 1.87, 'liquid', 85, None, ['caustic'])

