from itertools import count


def big_primefac_div(n):

    def prime(n):
        return all((n % i for i in range(2, int(n ** 0.5) + 1)))
    if n != int(n):
        return 'The number has a decimal part. No Results'
    if prime(abs(n)):
        return []
    f = factor(abs(n))
    return [max(f), abs(n) / f[0]]


def factor(n):
    (j, li) = (2, [])
    while j * j <= n:
        if n % j == 0:
            n //= j
            li.append(j)
        else:
            j += 1
    if n > 1:
        li.append(n)
    return li
