def starting_mark(height):
    # y = kx+d
    k = (10.67-9.45)/(1.83- 1.52)
    d = 9.45-k*1.52 
    return round(k*height+d,2)
