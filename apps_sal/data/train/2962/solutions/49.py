def divisible_by(numbers, divisor):
    listnew = []
    for x in numbers:
        if x % divisor == 0:
            listnew.append(x)
    return listnew
