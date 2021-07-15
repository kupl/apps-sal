def difference_of_squares(n):
    sum_up_to_n = n * (n + 1) // 2
    return sum_up_to_n ** 2 - sum(num ** 2 for num in range(1, n + 1))
