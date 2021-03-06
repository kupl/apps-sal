def modular_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = result * base % modulus
        exponent = exponent // 2
        base = base * base % modulus
    return result


def passesMillerRabinTest(n, a):
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d >>= 1
    x = modular_pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for ss in range(s - 1):
        x = x * x % n
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


primeList = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def isPrime(n):
    for p in primeList:
        if n % p == 0:
            return n == p
    for p in primeList:
        if passesMillerRabinTest(n, p) == False:
            return False
    return True


t = int(input())
for tt in range(t):
    n = int(input())
    if n == 2:
        print(2)
        continue
    if n % 2 == 0:
        n -= 1
    while True:
        if isPrime(n):
            print(n)
            break
        n -= 2
