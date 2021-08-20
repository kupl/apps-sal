def circular_permutations(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


def is_prime(n):
    return n == 2 or pow(2, n - 1, n) == 1


def circular_prime(n):
    return all((is_prime(c) for c in circular_permutations(n)))
