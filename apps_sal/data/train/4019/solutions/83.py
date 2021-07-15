def max_multiple(divisor, bound):
    #your code here
    N = 1 
    list1 = list(range(1, bound+1))
    for N1 in list1:
        if N1 % divisor == 0:
            if N < N1:
                N = N1
    return N            
            
    

