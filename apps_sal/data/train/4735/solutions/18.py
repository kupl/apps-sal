def keep_order(ary, val):

        
    if val not in ary:
    
        ary.append(val)
   
    ary.sort()
    
    return ary.index(val)

