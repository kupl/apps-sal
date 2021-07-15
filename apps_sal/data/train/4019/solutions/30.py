def max_multiple(divisor, bound):
    num_lst = []
    for i in range(1, bound+1):
        if i % divisor == 0:
            num_lst.append(i)
    return num_lst[-1]
        
    #your code here

