def is_divide_by(number, a, b):
    return not any((number % n for n in (a, b)))
