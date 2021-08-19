def prime_factors_count(num):
    factors_count = 0
    while num % 2 == 0:
        factors_count += 1
        num /= 2

    i = 3
    max_factor = num**0.5
    while i <= max_factor:
        while num % i == 0:
            factors_count += 1
            num /= i
            max_factor = num**0.5
        i += 2

    if num > 1:
        factors_count += 1
    return factors_count


def find_prime_numbers(max_num):
    if max_num == 0:
        return []

    is_prime = [True] * (max_num + 1)
    for i in range(4, max_num, 2):
        is_prime[i] = False
    is_prime[0], is_prime[1] = False, False

    next_prime = 3
    stop_at = max_num**0.5
    while next_prime <= stop_at:
        for i in range(next_prime * next_prime, max_num + 1, next_prime):
            is_prime[i] = False
        next_prime += 2

    prime_numbers = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            prime_numbers.append(i)
    return prime_numbers


def mobius(n):
    for i in find_prime_numbers(int(n**0.5) // 2 + 10):   # An empirical trick :)
        if n % (i * i) == 0:
            return 0
    if prime_factors_count(n) % 2 == 0:
        return 1
    return -1
