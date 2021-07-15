def move_zeros(array):
    newarr =[]
    zeroarr=[]
    for item in array:
        if item!= 0 or type(item)== bool :
            newarr.append(item)
        else:
            zeroarr.append(item)
            
            
    newarr.extend(zeroarr)
    return(newarr)
