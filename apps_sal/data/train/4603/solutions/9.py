def Ackermann(m,n):
    return (lambda m,n,s = lambda m,n,f:n+1 if m == 0 and n >= 0 else f(m-1,1,f) if m>0 and n == 0 else f(m-1,f(m,n-1,f),f) if m > 0 and n > 0 else None:s(m,n,s))(m,n)
