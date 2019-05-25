import numpy as np
import string
import random

chaine = "3:9:71:69:65:65:65:65:65:73|2:8:3:9:70:68:64:64:64:72|6:12:2:8:3:9:70:68:64:72|11:11:6:12:6:12:3:9:70:76|10:10:11:11:67:73:6:12:3:9|14:14:10:10:70:76:7:13:6:12|3:9:14:14:11:7:13:3:9:75|2:8:7:13:14:3:9:6:12:78|6:12:3:1:9:6:12:35:33:41|71:77:6:4:12:39:37:36:36:44|"
chainemodif = "3:9:71:69:65:65:65:65:65:73|2:8:3:9:70:68:64:64:64:72|6:12:2:8:3:9:70:68:64:72|11:11:6:12:6:12:3:9:70:76|10:10:11:11:67:73:6:12:3:9|14:14:10:10:70:76:7:13:6:12|3:9:14:14:11:7:13:3:9:75|2:8:7:13:14:3:9:6:12:78|6:12:3:1:9:6:12:3:1:9|71:77:6:4:12:7:5:4:4:12|"

tabsplit = chaine.split("|",10)
tabsplit.remove('')

tableau=[]
for i in tabsplit:
    tableau.append(i.split(":"))

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
for i in range(len(tableau)):
    for j in range(len(tableau[0])):
        val=int(tableau[i][j])
        if(val>=32):
            tableau[i][j]=0
        else:
            if(val>=8):
                val-=8
            if(val>=4):
                val-=4
            if(val==3):
                tableau[i][j]=alphabet[0]
                alphabet.pop(0)
            elif(val==2):
                tableau[i][j]=tableau[i-1][j]
            else:
                tableau[i][j]=tableau[i][j-1]

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
coord=[]
for i in alphabet:
    coord.append([])
for i in range(len(tableau)):
    for j in range(len(tableau[0])):
        val=tableau[i][j]
        if(val!=0):
            coord[string.ascii_lowercase.index(val)].append((i,j))

print(np.array(tableau))
print("")
print(coord)
print("")

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

print(toutCoup(coord,[(5,8),(2,1),(5,1)]))
print(tableau[2][1])

def nextAction(coupPossible):
    return coupPossible[random.randint(0,len(coupPossible)-1)]
    

print("")
for i in range(0,100):
    print(nextAction(toutCoup(coord,[(2,1),(5,1)])))