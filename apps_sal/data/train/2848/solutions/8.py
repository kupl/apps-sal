def N(Q,S,R,L,D,C,I) :
    if 0 < D and 0 < S :
        for I in range(I,L) :
            N(Q,S - Q[I],R,L,D - 1,C + (Q[I],),I)
    elif 0 == S :
        R.add(C)
    return R

def find (Q,S) :
    Q = sorted(set(Q))
    return len(N(Q,S,set(),len(Q),len(Q),(),0))
