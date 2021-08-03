def divisible_by(numbers, divisor):
    new = []
    for i in numbers:
        if i % divisor == 0:
            new.append(i)
    return new
