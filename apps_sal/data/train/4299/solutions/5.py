import math

def is_prime_happy(n):
    isPrime = [False, False] + [True] * (n-2)
    for k in range(2, n):
        for i in range(2, int(math.floor(math.sqrt(k)))+1):
            if isPrime[i] and k%i == 0:
                isPrime[k] = False
                break
    return True in isPrime and sum([k for k in range(n) if isPrime[k]]) % n== 0

