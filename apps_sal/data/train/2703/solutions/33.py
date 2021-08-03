def square_sum(numbers):
    lol = 0
    hassu = len(numbers)
    while hassu > 0:
        lol = numbers[hassu - 1] ** 2 + lol
        hassu = hassu - 1
    return lol
