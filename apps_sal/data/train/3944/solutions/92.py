def sum_triangular_numbers(n):
    # your code here
    return sum(sum(range(i)) for i in range(n + 2))
