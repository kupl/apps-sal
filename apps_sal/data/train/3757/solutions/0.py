from decimal import Decimal, ROUND_HALF_UP


def round_to_five(numbers):
    return [(n / 5).quantize(1, ROUND_HALF_UP) * 5 for n in map(Decimal, numbers)]
