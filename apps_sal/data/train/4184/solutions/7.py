primes=[2,3,5,7]

def is_prime(n):
    if n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if is_prime(i) and i not in primes:
            primes.append(i)
        if n % i == 0:
            return False
    return True
