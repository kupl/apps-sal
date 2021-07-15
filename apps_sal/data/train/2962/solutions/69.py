def divisible_by(numbers, divisor):
    new = list()
    for i in numbers:
        if i % divisor == 0:
            new.append(i)
    return new
