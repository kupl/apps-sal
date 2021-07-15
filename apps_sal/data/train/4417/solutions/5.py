N = 10 ** 5

def sum_square_digits(n):
    return sum((ord(d) - 48) ** 2 for d in str(n))

def reductible(n):
    suite = set()
    while n not in suite:
        suite.add(n)
        n = sum_square_digits(n)
    return n == 1

max_digit_sum = 81 * len(str(N))
sum_reduc = set(filter(reductible, range(max_digit_sum + 1)))

def primes(n):
    sieve = n // 2 * [True]
    for i in range(3, int(n**.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i*i // 2::i] = [False] * ((n - i*i - 1) // (2*i) + 1)
    return [2] + [2*i + 1 for i in range(1, n // 2) if sieve[i]]

prime_reduc = [n for n in primes(N) if sum_square_digits(n) in sum_reduc]

from bisect import bisect_left
def solve(a, b):
    return bisect_left(prime_reduc, b) - bisect_left(prime_reduc, a)
