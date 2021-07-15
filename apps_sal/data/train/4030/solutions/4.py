def radix_tree(*W):
    D={}
    for w in W:
        if w:D[w[0]]=D.get(w[0],[])+[w[1:]]
    Z={}
    for k in D:
        T=radix_tree(*D[k])
        if len(T)==1and''not in D[k]:
            for j in T:k,T=k+j,T[j]
        Z[k]=T
    return Z
