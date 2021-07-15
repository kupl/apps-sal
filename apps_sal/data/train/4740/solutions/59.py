def row_sum_odd_numbers(n):
    #your code here
    triNumber = n * (n + 1) / 2
    totalOdd = triNumber ** 2
    
    previousRow = n - 1
    
    previousTriNumber = previousRow * (previousRow + 1) / 2
    
    totalOddPrevious = previousTriNumber ** 2
    
    return totalOdd - totalOddPrevious
