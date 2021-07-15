def row_sum_odd_numbers(n):
    #your code here
    
    starting_no = 1 + sum([2*i for i in range (0, n)])
    
    return sum([starting_no + 2*i for i in range(0, n)])
