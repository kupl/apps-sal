def combos(n,r=0):
    if n < 2 or r == 1: return [[1]*n]
    return sum([[c+[i] for c in combos(n-i,i)] for i in range(1,min(n,r or n)+1)],[])
