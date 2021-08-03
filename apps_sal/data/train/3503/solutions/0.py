def dig_pow(n):
    return sum(int(x)**y for y, x in enumerate(str(n), 1))


def sum_dig_pow(a, b):
    return [x for x in range(a, b + 1) if x == dig_pow(x)]
