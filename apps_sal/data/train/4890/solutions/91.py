def find_difference(a, b):
    v1=1
    v2=1
    for i,j in zip(a,b):
        v1 = v1*i
        v2 = v2*j
        
    return abs(v1-v2)
