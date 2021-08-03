def close_compare(a, b, margin=0):
    if(a == b or (b - a <= margin and b - a >= 0) or (a - b <= margin and a - b >= 0)):
        return 0
    elif(a < b):
        return -1
    elif(a > b):
        return 1
