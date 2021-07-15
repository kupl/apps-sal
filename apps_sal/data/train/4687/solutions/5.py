def decomp(n):
    result = []
    for i in primes():
        if i > n:
            break
        count = 0
        for j in range(2, n+1):
            while j % i == 0:
                count += 1
                j = j / i
        if count > 1:
            result.append(str(i)+'^'+str(count))
        else:
            result.append(str(i))
    return ' * '.join(result)

def primes():
    yield 2
    it = odd()
    while True:
        n = next(it)
        yield n
        it = filter(lambda x,n=n: x % n > 0, it)
        
def odd():
    n = 1
    while True:
        n += 2
        yield n
