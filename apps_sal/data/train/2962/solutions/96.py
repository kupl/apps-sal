def divisible_by(numbers, divisor):
    s = list()
    for i in numbers:
        if i % divisor == 0:
            s.append(i)
    return s
