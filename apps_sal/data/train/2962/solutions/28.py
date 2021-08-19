def divisible_by(numbers, divisor):
    return list((x for x in numbers if not x % divisor))
