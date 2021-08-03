def divisible_by(numbers, divisor):
    z = []
    for k in numbers:
        if k % divisor == 0:
            z.append(k)
    return z
