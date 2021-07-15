def row_sum_odd_numbers(n):
    return sum([n*(n-1)+1+2*k for k in range(n)])
