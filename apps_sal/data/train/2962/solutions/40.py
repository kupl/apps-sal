def divisible_by(numbers, divisor):
    a = []
    for x in numbers:
        if x % divisor == 0:
            a.append(x)
        else:
            pass
    return a
