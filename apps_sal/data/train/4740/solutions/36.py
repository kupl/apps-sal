def row_sum_odd_numbers(n):
    return sum([n for n in range(n * (n + 1)) if n % 2 != 0][-n:])
