def divisible_by(numbers, divisor):
    tmp = []
    for i in numbers:
        if i%divisor ==0:
            tmp.append(i)
    return tmp
