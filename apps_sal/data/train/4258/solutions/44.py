def series_sum(n):
    return '%.2f'%series_sum_(n)
    
def series_sum_(n):
    if(n>1):
        return series_sum_(n-1)+float(float(1.00)/float(3*(n-1)+1))
    elif(n==1):
        return float(1.00)
    return float(0.00)

