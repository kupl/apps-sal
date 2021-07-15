from fractions import Fraction
def series_sum(n):
    
    sum=0
    
    for i in range(n):
        sum+=1/(1+i*3)
    
    return format(sum,'.2f')
