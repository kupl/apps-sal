def divisible_by(numbers, divisor):
    rez = []
    for x in numbers:
        if x % divisor == 0:
            rez.append(x)
    return rez

