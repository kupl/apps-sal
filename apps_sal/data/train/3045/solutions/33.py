def elevator(left, right, call):
    
    l = left
    r = right
    c = call
    
    if l == r or (l == 2 and r == 0 and c == 1) or (l == 0 and r == 2 and c == 1):
        return "right"
    elif l == c:
        return "left"
    elif l > c > r or r < c < l or c < l < r or c > l > r:
        return "left"
    else:
        return "right"
    

