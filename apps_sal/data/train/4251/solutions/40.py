def difference_of_squares(n):
    sum=0
    square=0
    for i in range(1,n+1):
        sum+=i**2
    
    for num in range(1,n+1):
        square+=num
        
    square**=2
    
    return(square-sum)
