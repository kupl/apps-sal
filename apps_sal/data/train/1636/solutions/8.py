def productsum(n):
    if n < 12:
        kmax = n+1
    else:
        kmax = n
    
    def prodsum(p, s, nf, start):
        k = p - s + nf     #product - sum + number of factors
        if k < kmax:
            if p < n[k]:
                n[k] = p
            for i in range(start, kmax//p*2 + 1):
                prodsum(p*i, s+i, nf+1, i)
    if kmax > 12: kmax +=1
    n = [2*kmax] * kmax
    
    prodsum(1, 1, 1, 2)
    
    return sum(set(n[2:]))
