def productsum(n):
    pass # Your code here
    
def productsum(kmax):
    def prodsum2(p, s, c, start):
        k = p - s + c     # product - sum + number of factors
        if k < kmax:
            if p < n[k]: n[k] = p
            for i in range(start, kmax//p*2 + 1):
                prodsum2(p*i, s+i, c+1, i)

    kmax += 1
    n = [2*kmax] * kmax
    prodsum2(1, 1, 1, 2)

    return sum(set(n[2:]))
