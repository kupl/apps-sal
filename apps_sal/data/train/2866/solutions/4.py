def mobius(n):
    a = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if isPrime(i):
                if n % (i * i) == 0:
                    return 0
                a += 1
            n = n // i
            if isPrime(n):
                a += 1
                break
    if a > 0 and a % 2 == 0:
        return 1
    return -1


def isPrime(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True
