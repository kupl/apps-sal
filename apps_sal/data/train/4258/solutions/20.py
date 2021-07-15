def series_sum(n):
    # Happy Coding ^_^
    sum=0.00
    if n==1:
        return("1.00")
    elif n==0:
        return("0.00")
    else:
        denominator=1.00
        for i in range(0,n):
            if (i+1) <= n:
                sum=sum+(1/denominator)
                denominator=denominator + 3.00
    
    return(str(format(round(sum,2),'.2f')))
