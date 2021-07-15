def sum_triangular_numbers(n):
    s = a = 0
    for i in range(1, n+1):
        a += i
        s += a
    
    return s
