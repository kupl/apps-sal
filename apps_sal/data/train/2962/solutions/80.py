def divisible_by(numbers, divisor):
    _ = filter(lambda num: num % divisor == 0, numbers)
    return list(_)
