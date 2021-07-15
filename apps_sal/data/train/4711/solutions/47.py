def zeros(n):
    divisor=5
    count=0
    while(n>divisor):
        count=count+int(n/divisor)
        divisor*=5
    return (count)
        
        

