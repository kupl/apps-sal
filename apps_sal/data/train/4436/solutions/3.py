def S2N(m,n):
    return sum(base**pow for pow in range(n+1) for base in range(m+1))
