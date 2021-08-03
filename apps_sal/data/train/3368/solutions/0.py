def circular_permutations(n):
    n = str(n)
    return [int(n[i:] + n[:i]) for i in range(len(n))]


def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def circular_prime(n):
    return all(is_prime(x) for x in circular_permutations(n))
