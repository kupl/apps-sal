def divisible_by(numbers, divisor):
    return list(filter(lambda numbers: not(numbers % divisor), numbers))
