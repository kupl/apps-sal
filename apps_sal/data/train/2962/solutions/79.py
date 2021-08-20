def divisible_by(numbers, divisor):
    i = 0
    a = []
    for item in numbers:
        if item % divisor == 0:
            a.insert(i, item)
            i += 1
    return a
