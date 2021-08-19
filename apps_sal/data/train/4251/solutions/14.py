def difference_of_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return (n * (n + 1) / 2) ** 2 - sum
