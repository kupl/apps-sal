def sort_by_area(seq): 
    
    valueList = []
    for i in seq:
        if isinstance(i,tuple):
            l1 = i[0]
            l2 = i[1]
            area = l1 * l2
        else:
            area = 3.14*i**2
        
        valueList.append(area)
        
    a = sorted(range(len(valueList)),key=valueList.__getitem__)    # Get index of sorted list
    sort_by_area =  [seq[i] for i in a]

    return sort_by_area
