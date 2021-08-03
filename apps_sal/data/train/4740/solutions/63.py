def row_sum_odd_numbers(n):
    num_add = n * (n + 1) / 2
    last = (num_add * 2) - 1
    first = last + 2 * (1 - n)
    return (first + last) * (n / 2)
