def genFib():
    a,b = 1,0
    while 1:
        yield a
        a,b = a+b,a

FIB,fib = [], genFib()

def getFib(m):
    while len(FIB)<m: FIB.append(next(fib))
    return FIB[:m]
        
        
def mysterious_pattern(m, n):
    lst = [v%n for v in getFib(m)]
    
    arr = [[' ']*m for _ in range(n)]
    for y,x in enumerate(lst): arr[x][y] = 'o'
    
    return '\n'.join(''.join(row).rstrip() for row in arr).strip('\n')

