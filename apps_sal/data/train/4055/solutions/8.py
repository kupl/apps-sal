def solve(n):
    FIB = ['0', '01']
    for _ in range(len(FIB), n+1): 
        FIB.append(FIB[-1] + FIB[-2])
    return FIB[n]
