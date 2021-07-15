def isprime(n):
    if n==2: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False 
    return True
sbs = []
for i in range(22):
    j = 0
    while 2**i * 3**j + 1 <= 1500000:
        if isprime(2**i * 3**j + 1):
            sbs.append(2**i * 3**j + 1)
        j += 1
def solve(x,y): return sum( x <= z & z <= y for z in sbs )
