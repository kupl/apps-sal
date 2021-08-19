def prime(n):
    return all((n % i for i in range(2, int(n ** 0.5) + 1)))


li = ''.join((str(i) for i in range(2, 10 ** 5) if prime(i)))


def solve(s, n):
    return ''.join(li)[s:s + n]
