def divisible_by(numbers, divisor):
    return list(filter(lambda el: not el % divisor, numbers))
