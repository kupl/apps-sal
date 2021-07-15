def isPP(n):
    for k in range(2,round(n**0.5+1)):
        m=round(n**(1/k))
        if m**k==n:
            return [m,k]
    return None
