def difference_of_squares(n):
    total = 0
    total_2 = 0
    for i in range(0, n + 1):
        total += int(i)
    total = total ** 2
    for i in range(0, int(n) + 1):
        total_2 += i ** 2
    return total - total_2
