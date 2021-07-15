def Ackermann(m,n):
    if m:
        if n:
            return Ackermann(m - 1, Ackermann(m, n - 1))
        return Ackermann(m - 1, 1)
    return n+1
