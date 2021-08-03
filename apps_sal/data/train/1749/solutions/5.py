def factors(number):
    div = 2
    while div * div <= number:
        cnt = 0
        while number % div == 0:
            cnt += 1
            number //= div
        if cnt:
            yield div, cnt
        div += 1
    if number != 1:
        yield number, 1


def get_prime_power(n, p):
    res = 0
    div = p
    while div <= n:
        res += n // div
        div *= p
    return res


def trailing_zeros(number, base):
    return min(get_prime_power(number, num) // cnt for num, cnt in factors(base))
