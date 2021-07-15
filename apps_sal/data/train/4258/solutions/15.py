def series_sum(n):
    return "{0:.2f}".format( sum(1.0/(1+(i-1)*3) for i in range(1,n+1)) )
