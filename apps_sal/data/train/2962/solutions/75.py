def divisible_by(numbers, divisor):
    a = []
    for el in numbers:
        if el % divisor == 0:
            a.append(el)
    return a
