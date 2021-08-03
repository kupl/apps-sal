def gap(g, m, n):
    for first in range(m, n - g + 1):
        found = True
        if is_prime(first):
            for second in range(first + 1, first + g):
                if is_prime(second):
                    found = False
                    break
            if found:
                if is_prime(first + g):
                    return [first, first + g]
    return None


def is_prime(n):
    for div in range(2, int(n**.5 + 1)):
        if (n / div).is_integer():
            return False
    return True
