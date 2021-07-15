def sum_triangular_numbers(n):
    addend,sum = 0,0,
    for step in range(1,n+1):
        addend += step
        sum += addend
    return sum
