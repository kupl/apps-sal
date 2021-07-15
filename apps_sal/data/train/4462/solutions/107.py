def adjacent_element_product(array):
    i=0
    b=0
    c=array[0]*array[1]
    while i < len(array)-1:
        b = array[i]*array[i+1]
        if b>c:
            c=b
            i+=1
        else:
            i+=1
    
    return c
