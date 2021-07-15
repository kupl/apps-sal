from itertools import combinations
from numpy.linalg import det

def find_biggTriang(listP):
    lp = list(map(list,listP))
    result = [0,0,0,[],0]
    result[0] = len(lp)
    lc = list(combinations(lp,3))
    result[1] = len(lc)
    n = 0
    for c in lc:
        l = list(c)
        m = [[l[0][0],l[0][1],1],[l[1][0],l[1][1],1],[l[2][0],l[2][1],1]]
        A = round((1/2)*abs(det(m)),1)
        if A == 0:
            n += 1
        elif A==result[4]:
            result[3].append(l)
        elif A>result[4]:
            result[4] = A
            result[3].clear()
            result[3].append(l)
    result[2] = result[1] - n
    result[3] = sorted(result[3])
    if len(result[3])==1:
        result[3] = result[3][0]
    return result
