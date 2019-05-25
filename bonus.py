import numpy as np
import string
import random

class IA:

    def __init__(self, map):
        self.map = map
        self.parcelleJouer = []

    def addParcelJouer(self, coup):
        for parcelle in self.map:
            if coup in parcelle:
                if parcelle not in self.parcelleJouer:
                    self.parcelleJouer.append(parcelle)

    def toutCoup(self, touteCoord, listeCoups = None):
        ret = []
        if listeCoups==None:
            for parcelle in touteCoord:
                for coordonnee in parcelle:
                    ret.append(coordonnee)
        else:
            for parcelle in touteCoord:
                parcelleJoue = False
                if(listeCoups[-1] in parcelle or listeCoups[-2] in parcelle):
                    parcelleJoue = True
                if not parcelleJoue:
                    for coordonnee in parcelle:
                        if listeCoups[-1][0] == coordonnee[0] or listeCoups[-1][1] == coordonnee[1]:
                            if coordonnee not in listeCoups:
                                ret.append(coordonnee)
        return ret

    def proba(self, coupPossible):
        ret = []
        for parcelle in self.parcelleJouer:
            if coupPossible not in parcelle:
                ret.append(coupPossible)
        return ret


    def nextAction(self, coupPossible, listeParcelleJouer):
        coup = proba(listeParcelleJouer, coupPossible)
        if len(coup) != 0:
            return coup[random.randint(0, len(coup) - 1)]
        return coupPossible[random.randint(0, len(coupPossible) - 1)]

