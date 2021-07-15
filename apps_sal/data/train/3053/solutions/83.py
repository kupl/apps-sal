def close_compare(a, b, margin = 0):
    c = abs(a-b)
    if c <= margin:
        return 0
    else:
        if a > b:
            return 1
        else:
            return -1
        
        
    pass
