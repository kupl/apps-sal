def is_divide_by(number, a, b):
    return sum(map(lambda n: number % n == 0, [a, b])) == 2
