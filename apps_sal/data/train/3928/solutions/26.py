def pro_recursive(n, m): 
    if n == 1: 
        return m
    else: 
        return m + pro_recursive(n-1, m)
        
def billboard(name, price=30): 
    return pro_recursive(len(name), price)
