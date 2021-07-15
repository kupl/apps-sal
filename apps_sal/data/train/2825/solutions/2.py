import numpy as np

def even_magic(n):
    mx    = n*n
    draft = np.arange(1, mx +1).reshape((n, n))
    art   = np.arange(mx, 0,-1).reshape((n, n))
    
    for i in range(n):
        for y in range(n):
            if any(( all((i%4 in [0,3], y%4 in [0,3])), all((i%4 in [1,2], y%4 in [1,2])) )):
                draft[i][y] = art[i][y]
                
    return draft.tolist()
