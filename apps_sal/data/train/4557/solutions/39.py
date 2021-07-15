def row_weights(array):
    
    x = 0
    t1 = []
    t2 = []
    
    for i in array:
        if x%2==0:
            t1.append(i)
        else:
            t2.append(i)
        x+=1
    
    return (sum(t1), sum(t2))
