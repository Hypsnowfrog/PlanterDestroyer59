import numpy as np
import string
import random

class IA:

    def __init__(self, chaine):
        self.chaine = chaine

    def toutCoup(touteCoord, listeCoups = None):
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

    def nextAction(coupPossible):
        return coupPossible[random.randint(0, len(coupPossible)-1)]
