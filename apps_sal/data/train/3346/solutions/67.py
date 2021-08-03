primes = {2, 3, 5, 7}
not_primes = {1, 4, }


def is_prime(z):
    if z in not_primes:
        return False
    elif z in primes:
        return True
    out = z & 1 and z % 3 and z > 10 and all(z % i and z % (i + 2) for i in range(5, 1 + int(z**0.5), 6))
    if out:
        primes.add(z)
    else:
        not_primes.add(z)
    return out


def gap(g, m, n):
    if g == 1 and m <= 2 and n >= 3:
        return [2, 3]
    if g & 1 or g > n - m:
        return None
    for i in range(m | 1, n + 1 - g, 2):
        if is_prime(i):
            for j in range(i + 2, i + g + 1, 2):
                if is_prime(j):

                    if j == i + g:
                        return [i, j]
                    else:
                        break
