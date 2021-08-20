def row_sum_odd_numbers(n):
    starting_no = 1 + sum([2 * i for i in range(0, n)])
    return sum([starting_no + 2 * i for i in range(0, n)])
