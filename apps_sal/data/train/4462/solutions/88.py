def adjacent_element_product(array):
    mults = []
    i = 0
    while i+1 < len(array):
        mults.append(array[i]*array[i+1])
        i += 1
    return max(mults)
    
        
        

