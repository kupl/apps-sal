def addInDict(x, y):
    nonlocal d, d2
    if x not in d:
        d[x] = 0
    if x not in d2[y]:
        d2[y][x] = 0
    d[x] += 1
    d2[y][x] += 1

def calcSum1():
    nonlocal d, d2, d3, d4, d4Keys, s1, s2
    for kol in d4Keys:
        for numPart in d4[kol]:
            kol1 = d[numPart]
            while kol1 in d3 and kol1 > 0:
                kol1 -= 1
            if kol1 > 0:
                d3[kol1] = 1
                s1 += kol1
                s2 += min(kol, kol1)
                if numPart in d2[0]:
                    del d2[0][numPart]
            
            
def calcSum0():
    nonlocal d, d2, d3, s1, s2
    for key in d2[0]:
        kol = d[key]
        while kol in d3 and kol > 0:
            kol -= 1
        if kol > 0:
            d3[kol] = 1
            s1 += kol

import sys
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    d, d2, d3, d4 = {}, {}, {}, {}
    d2[0] = {}
    d2[1] = {}
    for __ in range(n):
        a, f = list(map(int, sys.stdin.readline().split()))
        addInDict(a, f)
##    print('d=', d)
##    print('d2=', d2)
    s1, s2 = 0, 0
    for i in d2[1]:
        if d2[1][i] not in d4:
            d4[d2[1][i]] = {}
        d4[d2[1][i]][i] = i
##    print('d4=', d4)
    d4Keys = list(d4.keys())
    d4Keys.sort(reverse = True)
##    print('d4Keys=', d4Keys)
    
    calcSum1()
    calcSum0()
    print(s1, s2)

