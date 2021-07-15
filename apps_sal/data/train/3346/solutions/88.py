def gap(g, m, n):
    l1=0
    for i in range(m,n+1):
        l2=l1
        if isPrime(i):
            l1=i
            if l1-l2 ==g and l2!=0:
                return [l2,l1]
def isPrime(n):
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True
