def row_sum_odd_numbers(n):
    rowStart = n*(n-1) + 1
    total = 0
    for i in range(n):
        total = total + (rowStart + 2 * i)
        
    return total
