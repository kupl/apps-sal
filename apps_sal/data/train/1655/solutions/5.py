import numpy as np
from itertools import combinations

def ctri(lst):
    if len(lst)<3:
        return 0
    return sum(1 for j in combinations(lst, 3) if abs(np.linalg.det(np.mat([i+[1] for i in j])))>1e-3)

def count_col_triang(ipt):
    d = {}    
    for i in ipt:
        if i[1] not in d:
            d[i[1]] = [i[0]]
        else:
            d[i[1]].append(i[0])

    p = {i:ctri(d[i]) for i in d}
    pmax = max(p.values())
    
    plst = [] if pmax == 0 else sorted([i for i in p if p[i]==pmax]) + [pmax]
    return [len(ipt), len(p), sum(p.values()), plst]
