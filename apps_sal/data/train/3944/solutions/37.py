def sum_triangular_numbers(n):
    # your code here
    return sum([(i + 1) * i / 2 for i in range(1, n + 1)])
