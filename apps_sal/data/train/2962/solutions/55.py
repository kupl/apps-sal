def divisible_by(a, b):
    return [*filter(lambda n: n % b == 0, a)]
