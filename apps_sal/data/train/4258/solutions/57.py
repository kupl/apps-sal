def series_sum(n):
    x=1 
    s=0
    for i in range(n):
       
        s+= 1/(x+i*3)
    if s==0:
        return '0.00'
    if len(str(round(s,2))) <4:
        return str(round(s,2))+'0'
    
    return str(round(s,2))
