def row_sum_odd_numbers(n, base=2):
    first_num = (n * (n - 1)) + 1
    numbers = range(first_num, first_num + base * n, base)
    return sum(numbers)
