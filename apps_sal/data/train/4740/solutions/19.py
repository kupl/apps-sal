def row_sum_odd_numbers(n):
    x = 1
    r = 1
    inc = 2
    s = 0
    
    for i in range(1, n):
        x += inc
        r += 1
        inc += 2
    
    for j in range(r):
        s += x
        x += 2
        
    return s
