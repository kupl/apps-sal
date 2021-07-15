def row_sum_odd_numbers(n):
    """the sum of all odd numbers in a row
    is actually the row number cubed"""
    if n < 1:
        return 0
    else:
        return n*n*n
