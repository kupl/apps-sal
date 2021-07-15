def close_compare(a, b, margin=0):
    res = abs(a-b)
    
    if res <= margin:
        return 0
    else:
        if a < b:
            return -1
        elif a==b:
            return 0
        else:
            return 1
