def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gap(g, m, n):
    first_prime = 0
    second_prime = 0
    for i in range(m, n + 1):
        if i % 2 == 0:
            continue
        if is_prime(i) and first_prime == 0:
            first_prime = i
        elif is_prime(i) and first_prime != 0:
            second_prime = i
        if second_prime != 0 and second_prime - first_prime == g:
            return [first_prime, second_prime]
        elif second_prime != 0 and second_prime - first_prime != g:
            first_prime = second_prime
            second_prime = 0
    return None
