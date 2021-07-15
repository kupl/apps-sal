def row_sum_odd_numbers(n):
    
    x = 1
    c = 0
    final = 0
    
    for e in range(n):
        x += c
        c += 2
        
    for d in range(n):
        final += x
        x += 2
        
    return final
