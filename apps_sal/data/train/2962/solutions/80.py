def divisible_by(numbers, divisor):
    #numbers
    _ =         filter(lambda num: num % divisor == 0,                     numbers)

    return list(_)
