def sum_triangular_numbers(n):
    return 0 if n < 0 else int(1/6*n*(n+1)*(n+2)+1e-5)
