def sum_triangular_numbers(n):
    m = abs(n)
    if m == n:
        sum_ = 0
        while n > 0:
            sum_ += (n * (n+1) / 2)
            n -= 1
    else: sum_ = 0
    return sum_
