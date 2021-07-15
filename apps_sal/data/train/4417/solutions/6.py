def isprime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
def solve(a,b):
    count = 0
    for i in range(a,b):
        if isprime(i):
            c = 0
            while i!=1 and c!= 10:
                i = sum(int(j)**2 for j in list(str(i)))
                c += 1
            if i==1:
                count += 1
    return count
