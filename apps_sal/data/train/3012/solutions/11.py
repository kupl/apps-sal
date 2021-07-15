def shared_bits(a, b):
    
    x = "{0:016b}".format(min(a,b))
    y = "{0:016b}".format(max(a,b))
    sol=0
    
    for i in range(len(x)):
        if x[i] == "1" and y[i] == "1":
            sol+=1
    
    return sol>=2
