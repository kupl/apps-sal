def max_multiple(divisor, bound):
    lst  = []
    
    for num in range(divisor,bound+1):
        if num % divisor == 0:
            if num <= bound:
                lst.append(num)
                
    return lst[-1]
