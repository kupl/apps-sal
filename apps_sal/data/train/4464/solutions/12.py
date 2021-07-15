def feast(beast, dish):
    # your code here
    pass
    b = beast.replace(" ","")
    length_b = len(b)
    
    d = dish.replace(" ","")
    length_d = len(d)
    
    new_b = b[0] + b[-1]
    new_d = d[0] + d[-1]
    
    return new_b == new_d
