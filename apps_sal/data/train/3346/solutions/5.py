def gap(g, m, n):
    for i in range(m, n):
        if isprime(i): # prime
            if isprime(i + g): # prime at gap
                if not any(list([isprime(x) for x in (list(range(i + 1, i + g)))])): # no prime inbetween              
                   return [i, i + g]
        
        
def isprime(x):
    if x <= 1 or x % 2 == 0:
        return False
    d = 3
    while d * d <= x:
        if x % d == 0:
            return False
        d = d + 2
    return True 

