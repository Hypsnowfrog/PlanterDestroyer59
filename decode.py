import re

def convert(char):
    if char == 'A':
        return 0
    elif char == 'B':
        return '1'
    elif char == 'C':
        return '2'
    elif char == 'D':
        return '3'
    elif char == 'E':
        return '4'
    elif char == 'F':
        return '5'
    elif char == 'G':
        return '6'
    elif char == 'H':
        return '7'
    elif char == 'I':
        return '8'
    elif char == 'J':
        return '9'


def decode(map):
    print(map)
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
    print(tab)
    return plot


# map = '3:1:1:1:9:3:1:1:1:9|2:0:0:0:8:2:0:0:0:8|2:0:0:0:8:2:0:0:0:8|2:0:0:0:8:2:0:0:0:8|6:4:4:4:12:6:4:4:4:12|'
map = '3:9:71:69:65:65:65:65:65:73|2:8:3:9:70:68:64:64:64:72|6:12:2:8:3:9:70:68:64:72|11:11:6:12:6:12:3:9:70:76|10:10:11:11:67:73:6:12:3:9|14:14:10:10:70:76:7:13:6:12|3:9:14:14:11:7:13:3:9:75|2:8:7:13:14:3:9:6:12:78|6:12:3:1:9:6:12:35:33:41|71:77:6:4:12:39:37:36:36:44|'
print(process(decode(re.search("([0-9]+([:\|]))+", map).group(0))))
