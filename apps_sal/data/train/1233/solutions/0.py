import sys

def GRIG(L):

    LENT = len(L)
    MINT = 1
    GOT = 0

    DY = [ [{x: 0 for x in range(0, 10)}, 0, 0] ]

    for i in L:

        DY.append([{x: 0 for x in range(0, 10)}, 0, 0])
        GOT += 1

        for j in range(0, GOT):

            if DY[j][0][i] == 1:
                DY[j][0][i] = 0
                DY[j][1] -= 1
            else:
                DY[j][0][i] = 1
                DY[j][1] += 1

            DY[j][2] += 1

            if DY[j][1] <= 1 and DY[j][2] > MINT:
                MINT = DY[j][2]

    return MINT

TESTCASES = int(input().strip())

for i in range(0, TESTCASES):
    
    L = [int(x) for x in list(input().strip())]
    
    print(GRIG(L))

