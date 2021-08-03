def divisible_by(numbers, divisor):
    num = []
    for i in numbers:
        x = i / divisor
        y = x - int(x)
        if y == 0:
            num.append(i)
    return num
