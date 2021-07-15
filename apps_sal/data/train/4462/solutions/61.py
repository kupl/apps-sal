def adjacent_element_product(array):
    maxp=None
    i=1
    while i<len(array):
        product=array[i]*array[i-1]
        if maxp==None or product>maxp:
            maxp=product
        i=i+1
    return maxp
