M = [[1] * 1800]
for V in range(2,1801) :
    U = [0]
    for F,B in enumerate(M[-1]) :
        if F < 1799 : U.append(0 if 1 + F < V else B + V * U[-1])
    M.append(U)
def combs_non_empty_boxesII(Q) :
    R = [0,0,0]
    for V in range(Q) :
        T = M[V][Q]
        R[0] += T
        if R[1] <= T : R[1:] = T,1 + V
    return R
