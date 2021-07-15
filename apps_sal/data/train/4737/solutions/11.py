def fuel_price(l, p):
    if l < 2:
        return round(l*p,2)
    if 2 <= l < 4:
        return round(l*(p-0.05),2)
    if 4 <= l < 6:
        return round(l*(p-0.1),2) 
    if 6 <= l < 8:
        return round(l*(p-0.15),2) 
    if 8 <= l < 10:
        return round(l*(p-0.2),2) 
    else:
        return round(l*(p-0.25),2)
