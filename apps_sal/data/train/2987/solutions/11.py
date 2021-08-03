def is_divide_by(number, *divisors):
    return not sum(map(lambda n: number % n != 0, divisors))
