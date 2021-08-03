def divisible_by(numbers, divisor):
    n = []
    for x in numbers:
        if x % divisor == 0:
            n.append(x)
    return n
