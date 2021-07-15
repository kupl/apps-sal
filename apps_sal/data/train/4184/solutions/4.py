primes = [2, 3, 5]
lastCheck = [6]

def is_prime(x):
    f = lastCheck[0]
    if x <= f:
        return x in primes
    limit = x ** 0.5
    for prime in primes:
        if prime > limit:
            return True
        if x % prime == 0:
            return False
    isPrime = True
    while f <= limit:
        f1 = f + 1
        if is_prime(f1):
            primes.append(f1)
        if x % f1 == 0:
            isPrime = False
        f5 = f + 5
        if is_prime(f5):
            primes.append(f5)
        if x % f5 == 0:
            isPrime = False
        f += 6
        if not isPrime:
            break
    lastCheck[0] = f
    return isPrime
