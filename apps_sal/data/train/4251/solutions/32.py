def difference_of_squares(n):
    nat_num=0
    for i in range(0,n+1):
        nat_num += i
    sqr_nat = nat_num **2
    
    sum_sqr = 0
    for b in range(0,n+1):
        sum_sqr += b**2
    
    
        
    return sqr_nat - sum_sqr
