def row_weights(array):
    a=0
    b=0
    for i in range(len(array)):
        if i%2==1:
            a=a+array[i]
        elif i%2==0:
            b=b+array[i]
    return (b,a)        
                

