def isPrime(n):
    if n in [1,4,6]:
        return False
    if n in [2,3,5,7]:
        return True
    if n % 3 == 0 or n % 2 == 0:
        return False
    k,a,b = 1,0,0
    sr = int(n ** 0.5)
    while b < sr:
        a = 6 * k - 1
        b = 6 * k + 1
        if n % a == 0 or n % b == 0:
            return False
        
        k += 1
    return True

def gap(g, m, n):
    curr, prev = 0,0
    for i in range(m,n+1):
        if isPrime(i):
            prev = curr
            curr = i
            if abs(prev - curr) == g and prev != 0:
                return [prev,curr]
    return None
            

