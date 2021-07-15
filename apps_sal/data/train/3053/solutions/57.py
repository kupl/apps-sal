def close_compare(a, b, margin = 0):
    if abs(a - b) <= margin:
        return 0
    else:
        if a > b:
            return 1
        if a < b:
            return -1
        
        
    

