def difference_of_squares(n):
    return (n * (n + 1) // 2) ** 2 - sum(x ** 2 for x in range(1, n + 1))
