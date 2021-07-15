def sum_triangular_numbers(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    calc = 1
    inc = 2
    sm = 1
    for x in range(2,n + 1):
        calc = calc + inc 
        sm = sm + calc
        inc = inc + 1
    return sm

