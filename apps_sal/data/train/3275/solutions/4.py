def clonewars(n):
    if n == 0: return [1,0]
    return [2**(n-1), 2**(n+1) - (n+1) - 1]
