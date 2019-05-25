import numpy as np
import string
import random

class IA:

    def __init__(self, map):
        self.map = map
        self.parcelleJouer = []
        self.coupJouer = []

    def addParcelJouer(self, coup):
        self.coupJouer.append(coup)
        for parcelle in self.map:
            if coup in parcelle:
                if parcelle not in self.parcelleJouer:
                    self.parcelleJouer.append(parcelle)

    def toutCoup(self):
        ret = []
        if len(self.coupJouer) == 0:
            for parcelle in self.map:
                for coordonnee in parcelle:
                    ret.append(coordonnee)
        else:
            for parcelle in self.map:
                parcelleJoue = False
                if self.coupJouer[-1] in parcelle:
                    parcelleJoue = True
                if len(self.coupJouer)>1 and self.coupJouer[-2] in parcelle:
                    parcelleJoue = True
                if not parcelleJoue:
                    for coordonnee in parcelle:
                        if self.coupJouer[-1][0] == coordonnee[0] or self.coupJouer[-1][1] == coordonnee[1]:
                            if coordonnee not in self.coupJouer:
                                ret.append(coordonnee)
        return ret

    def proba(self, coupPossible):
        ret = []
        for parcelle in self.parcelleJouer:
            if coupPossible not in parcelle:
                ret.append(coupPossible)
        return ret

    def nextAction(self):
        coupPossible = self.toutCoup()
        coup = self.proba(coupPossible)
        if len(coup) != 0:
            return coup[random.randint(0, len(coup) - 1)]
        return coupPossible[random.randint(0, len(self.toutCoup()) - 1)]

