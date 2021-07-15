def sum_triangular_numbers(n):
    step,addend,sum = 0,0,0
    for _ in range(n):
        step += 1
        addend += step
        sum += addend
    return sum    
