def row_sum_odd_numbers(n):
    #your code here
    
    a=[i for i in range(n*(n+1)) if i%2!=0]
    return sum(a[:-n-1:-1])
        

