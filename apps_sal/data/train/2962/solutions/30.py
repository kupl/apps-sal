def divisible_by(numbers, divisor):
    a = list((x for x in numbers if x % divisor == 0))
    return a
