def difference_of_squares(n):
    fuck = sum(range(n + 1)) ** 2
    cunt = sum(map(lambda x: x ** 2, range(1, n + 1)))
    return fuck - cunt
