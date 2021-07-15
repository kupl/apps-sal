primes = {p for p in range(3, 10001, 2) if all(p % i for i in range(3, int(p**0.5) + 1, 2))}
odd_not_prime_ = [i % 2 and i not in primes for i in range(1, 10001)]

def odd_not_prime(n):
    return sum(odd_not_prime_[:n])
