def divisible_by(numbers, divisor):
    c = []
    for number in numbers:
        if number % divisor == 0:
            c.append(number)
    return c
