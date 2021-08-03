import sys


def GRIG(L):

    MINT = 1
    GOT = 0

    DY = [[set(), 0, 0]]
    L_DY = 0

    for i in L:

        L_DY += 1
        DY.append([set(), 0, 0])

        for j in range(L_DY - 1, -1, -1):
            if i in DY[j][0]:
                DY[j][0].remove(i)
                DY[j][1] -= 1
            else:
                DY[j][0].add(i)
                DY[j][1] += 1

            DY[j][2] += 1
            if (DY[j][2] > MINT and DY[j][1] <= 1):
                MINT = DY[j][2]

    return MINT


TESTCASES = int(input().strip())

for i in range(0, TESTCASES):

    L = [int(x) for x in list(input().strip())]

    print(GRIG(L))
