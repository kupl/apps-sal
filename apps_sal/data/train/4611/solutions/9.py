def animals(heads, legs): 
    a= (4*heads-legs)/2
    b= (legs-2*heads)/2
    if  a==int(a) and  0 <=  a<= 1000 and  0 <=  b <=1000 and  b==int(b):
        return (a,b) 
    else:
        return'No solutions'
