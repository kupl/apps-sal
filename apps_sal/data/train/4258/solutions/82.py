def series_sum(n):
    sum = 1.00
    if n == 1:
        return('1.00')
    elif n==0: return('0.00')
    else:
        for x in range(1,n):
            sum = sum + (1/((2*(x+1))+(x-1)))
        return("{:.2f}".format(sum))
    

