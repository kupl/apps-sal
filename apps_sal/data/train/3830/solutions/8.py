def chain_arith_deriv(start, k):
    if is_prime(start):
        return '{} is a prime number'.format(start)
    (chain, n) = ([], float(start))
    for i in range(k):
        chain.append(n)
        n = sum((n * v / k for (k, v) in list(prime_factors_dict(n).items())))
        if n == 1:
            break
    return chain + [1] * (k - len(chain))


def is_prime(num):
    return num == 2 or (num > 2 and all((num % i for i in range(2, int(num ** 0.5) + 1))))


def prime_factors_dict(n):
    (d, exp) = ({}, 0)
    while n % 2 == 0:
        exp += 1
        n //= 2
    if exp:
        d[2] = exp
    for i in range(3, int(n ** 0.5) + 1):
        exp = 0
        while n % i == 0:
            exp += 1
            n //= i
        if exp:
            d[i] = exp
    if n > 1:
        d[n] = 1
    return d
