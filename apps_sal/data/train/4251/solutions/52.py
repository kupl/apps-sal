def difference_of_squares(n):
    return (n * (n + 1) // 2) ** 2 - sum((i ** 2 for i in range(1, n + 1)))
