def sieve(n):
    n = n - 1
    primes = [True for i in range(n + 1)]
    result = []
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    for p in range(2, n + 1):
        if primes[p]:
            result.append(p)
    return result


def prime_maxlength_chain(n):
    prime_num = sieve(n)
    prime_sums = [[0, 2]]
    count_max = 0
    results = []
    if n == 0:
        return []
    i, j = 0, 0

    while sum(prime_num[i:count_max + i + j]) < n:
        while sum(prime_num[i:count_max + i + j]) < n:
            count = len(prime_num[i:count_max + i + j])
            summe = sum(prime_num[i:count_max + i + j])
            if summe in prime_num:
                prime_sums.append([count, summe])

            j += 1
        if count_max <= prime_sums[-1][0]:
            count_max = prime_sums[-1][0]
        i += 1
        j = 0
    prime_sums.sort()
    for p in prime_sums:
        if p[0] == prime_sums[-1][0]:
            results.append(p[1])

    return results
