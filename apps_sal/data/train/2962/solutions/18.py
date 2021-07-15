def divisible_by(numbers, divisor):
    map = []
    for i in numbers:
        if i % divisor == 0:
            map.append(i)
    return map
