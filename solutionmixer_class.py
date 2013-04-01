#! /usr/bin/python
# coding: utf8
# Programm um die Anteile zweier Lösungen zu berechnen zur Erstellung einer Ziellösung mit gewünschter Konzentration

# Import Module
import time
#import chems
#import re
import chemicals

class GenericChemical(object):
    def __init__(self, mass, structur, dense, physcon):
        self.name = __init__.name
        self.mass = None
        self.structur = None
        self.dense = None
        self.physcon = None




# Variablen
solution1 = raw_input("Wähle Chemiekalie I: ")
concentration1 = float(raw_input("Wähle Konzentration von I in %: "))
#mol1 = float(raw_input("Wähle molare Masse von I in g mol^-1: "))
solution2 = raw_input("Wähle Chemiekalie II: ")
concentration2 = float(raw_input("Wähle Konzentration von II in %: "))
#mol2 = float(raw_input("Wähle molare Masse von II in g mol^-1: "))
concentration_aim = float(raw_input("Wähle Zielkonzentration in %: "))
#solution_aim =
menge = float(raw_input("Wähle die Menge deiner Ziellösung in g: "))
#molar = float(raw_input("Gib die Molare Masse: "))

# Funktionen
def mischung(concentration1, concentration2, concentration_aim):
        anteil1 = concentration_aim - concentration2
        anteil2 = concentration1 - concentration_aim
        gesamtteil = anteil1 + anteil2
        return anteil1, anteil2, gesamtteil

def calcmass(menge):
        gesamtteil = mischung(concentration1, concentration2, concentration_aim)[2]
        verhaeltnis = menge / gesamtteil
        anteil1 = mischung(concentration1, concentration2, concentration_aim)[0]
        anteil2 = mischung(concentration1, concentration2, concentration_aim)[1]
        masse1 = verhaeltnis * anteil1
        masse2 = verhaeltnis * anteil2
        return masse1, masse2

"""
def molarconv(menge, mol1, mol2):
        masse1 = calcmass(menge)[0]
        masse2 = calcmass(menge)[1]
        mol =
        return vol1, vol2
"""

"""
def datenbank(dbool,):

    return
"""


# Main-Funktion
if __name__ == '__main__':
    #mische = mischung(concentration1, concentration2, concentration_aim)[0]

    """

    if re.match("^[S|s]alzs[ä|ae]ure$", solution1):
        dbool = bool(raw_input('Soll Chemiekalie aus der Datenbank übernommen werden? [y/n]'))
    else:
        print 'Ihr verdammten Wichser !'

    """
    print '\n'
    print 'Mischen von chemischen Lösungen \n'
    print 'Deine Chemiekalie I ist %s mit einer Konzentration von %.2f %%' % (solution1, concentration1)
    #print 'Deine Chem I ist ' , solution1, 'mit Konz ', concentration1
    print 'Deine Chemiekalie II ist %s mit einer Konzentration von %.2f %%' % (solution2, concentration2)
    print 'Deine Zielkonzentration ist %.2f %%' % (concentration_aim)
    print 'Du möchtest eine Ziellösung von %.2f g herstellen' % menge
    print '****************** CALCULATING ******************\n'
    time.sleep(3)
    anteil1 = mischung(concentration1, concentration2, concentration_aim)[0]
    anteil2 = mischung(concentration1, concentration2, concentration_aim)[1]
    masse1 = calcmass(menge)[0]
    masse2 = calcmass(menge)[1]

    con_check1 = concentration1 < concentration_aim and concentration2 < concentration_aim
    con_check2 = concentration1 > concentration_aim and concentration2 > concentration_aim
    if con_check1 or con_check2:
        print 'xxxxxxxxxxxxxxxxxx IMPOSSIBLE xxxxxxxxxxxxxxxxxxx\n'
        print ' check your initial solutions\' concentrations\n'
        print 'xxxxxxxxxxxxxxxxxx IMPOSSIBLE xxxxxxxxxxxxxxxxxxx\n'
    else:
        print 'Du benötigst %.2f Teile / %.2f g von %s' % (anteil1, masse1, solution1)
        print 'und %.2f Teile / %.2f g von %s' % (anteil2, masse2, solution2)

