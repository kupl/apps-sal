def difference_of_squares(n):
    return sum(list(range(1, n + 1))) ** 2 - sum([num ** 2 for num in range(1, n + 1)])
