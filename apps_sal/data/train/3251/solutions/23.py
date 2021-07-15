from collections import defaultdict


def is_prime(a):
    return all(a % i for i in range(2, a))


def primeFactors(n):
    factors = defaultdict(int)
    rest = n
    while rest != 1:
        for num in range(2, rest+1):
            if rest % num == 0 and is_prime(num):
                factors[num] += 1
                rest //= num
                break

    return ''.join(
        map(
            lambda nc: '({}**{})'.format(nc[0], nc[1]) if nc[1] > 1 else '({})'.format(nc[0]),
            sorted(factors.items(), key=lambda x: x[0])
        )
    )
