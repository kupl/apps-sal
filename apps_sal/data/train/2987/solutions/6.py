def is_divide_by(number, *divisors):
    return all((number % divisor == 0 for divisor in divisors))
