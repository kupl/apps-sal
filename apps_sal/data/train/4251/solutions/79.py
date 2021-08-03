def difference_of_squares(n):
    summa = 0
    atseviski = 0
    for i in range(1, n + 1):
        summa += i
    summa = summa ** 2
    for x in range(1, n + 1):
        atseviski += x**2
    return abs(summa - atseviski)
