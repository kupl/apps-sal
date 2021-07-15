def nth_smallest(arr, pos):    
    if pos>-1 and pos<len(arr)+1:
        return sorted(arr)[pos-1]
    else:
        return -1
