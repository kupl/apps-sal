def divisible_by(numbers, divisor):
    lst = []
    for n in numbers:
        if n % divisor == 0:
            lst += [n]
    return lst
