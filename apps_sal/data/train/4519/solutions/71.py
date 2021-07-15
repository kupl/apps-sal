def max_number(n):
    
    sz = str(n)
    s = [char for char in sz]
    r = sorted(s, reverse = True)
    j = ''.join(r)
    
    return int(j)
