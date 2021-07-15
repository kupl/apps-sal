def close_compare(a, b, margin=0):
    
    if margin<b-a:
        return -1
    if margin<a-b:
        return 1
    if margin>=abs(a-b):
        return 0

