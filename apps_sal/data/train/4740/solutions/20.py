def row_sum_odd_numbers(n: int):
    """ Calculate the row sums of this triangle from the row index (starting at index 1). """
    return sum([_ for _ in range(n * (n - 1), n * (n - 1) + (n * 2)) if _ % 2])

