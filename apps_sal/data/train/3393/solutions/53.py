CACHE = [[i,sum([x**2 for x in range(1,i+1) if not(i%x)])] for i in range(1,10000) if sum([x**2 for x in range(1,i+1) if not(i%x)])**0.5 % 1 == 0]

def list_squared(m, n):
    return [e for e in CACHE if m <= e[0] <= n]
