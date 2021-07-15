def row_sum_odd_numbers(n):
    return sum([i for i in range(sum([i for i in range(1, n+1)])*2) if i % 2][:-n-1:-1])

