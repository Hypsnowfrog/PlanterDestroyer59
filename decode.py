import re


def convert(string):
    #Entré string 'A:1'
    if string[0] == 'A':
        return int(string[2]), 0
    elif string[0] == 'B':
        return int(string[2]), 1
    elif string[0] == 'C':
        return int(string[2]), 2
    elif string[0] == 'D':
        return int(string[2]), 3
    elif string[0] == 'E':
        return int(string[2]), 4
    elif string[0] == 'F':
        return int(string[2]), 5
    elif string[0] == 'G':
        return int(string[2]), 6
    elif string[0] == 'H':
        return int(string[2]), 7
    elif string[0] == 'I':
        return int(string[2]), 8
    elif string[0] == 'J':
        return int(string[2]), 9


def decode(map):
    lines = map.split('|')
    lines.pop()
    tab = []
    for line in lines:
        tab.append(line.split(':'))
    return tab


def wall(case):
    tmp = bin(int(case))[2:].zfill(4)
    if len(tmp) > 4:
        return ''
    return tmp


def rec(tab, res, x, y):
    res.append((x, y))
    w = wall(tab[x][y])
    tab[x][y] = -1
    if w != '':
        if w[0] != '1' and len(tab[0]) > y + 1:
            if (x, y + 1) not in res:
                rec(tab, res, x, y + 1)
        if w[1] != '1' and len(tab) > x + 1:
            if (x + 1, y) not in res:
                rec(tab, res, x + 1, y)
        if w[2] != '1' and y - 1 >= 0:
            if (x, y - 1) not in res:
                rec(tab, res, x, y - 1)
        if w[3] != '1' and x - 1 >= 0:
            if (x - 1, y) not in res:
                rec(tab, res, x - 1, y)


def process(tab):
    plot = []
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] != -1 and int(tab[i][j]) < 32:
                plot.append([])
                rec(tab, plot[-1], i, j)
    return plot

def convertStringInt(chaine):
    tabsplit = chaine.split("|", 10)
    tabsplit.remove('')
    tableau = []
    for i in range(len(tabsplit)):
        tableau.append(tabsplit[i].split(":"))
        tableau[i] = [int(j) for j in tableau[i]]
    return tableau

def convertPos(pos):
    print(pos)
    if pos[0] == 0:
        return 'A:'+str(0)
    elif pos[0] == 1:
        return 'B:'+str(1)
    elif pos[0] == 2:
        return 'C:'+str(2)
    elif pos[0] == 3:
        return 'D:'+str(3)
    elif pos[0] == 4:
        return 'E:'+str(4)
    elif pos[0] == 5:
        return 'F:'+str(5)
    elif pos[0] == 6:
        return 'G:'+str(6)
    elif pos[0] == 7:
        return 'H:'+str(7)
    elif pos[0] == 8:
        return 'I:'+str(8)
    elif pos[0] == 9:
        return 'J:'+str(9)

# map = '3:1:1:1:9:3:1:1:1:9|2:0:0:0:8:2:0:0:0:8|2:0:0:0:8:2:0:0:0:8|2:0:0:0:8:2:0:0:0:8|6:4:4:4:12:6:4:4:4:12|'
#map = '3:9:71:69:65:65:65:65:65:73|2:8:3:9:70:68:64:64:64:72|6:12:2:8:3:9:70:68:64:72|11:11:6:12:6:12:3:9:70:76|10:10:11:11:67:73:6:12:3:9|14:14:10:10:70:76:7:13:6:12|3:9:14:14:11:7:13:3:9:75|2:8:7:13:14:3:9:6:12:78|6:12:3:1:9:6:12:35:33:41|71:77:6:4:12:39:37:36:36:44|'
#print(process(decode(re.search("([0-9]+([:\|]))+", map).group(0))))
