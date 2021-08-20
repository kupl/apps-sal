def sum_triangular_numbers(n):
    (sum_, t_i) = (0, 0)
    for i in range(1, n + 1):
        t_i += i
        sum_ += t_i
    return sum_
