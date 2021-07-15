import numpy as np
def covered_pawns(pawns):
    n = len(pawns)
    p = np.zeros(n)
    for i in range(0,n):
        for j in range(0,n):
            if int(pawns[j][1]) == int(pawns[i][1])+1 and abs(ord(pawns[j][0])-ord(pawns[i][0])) == 1:
                p[j] = 1
    return sum(p)

