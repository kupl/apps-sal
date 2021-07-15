import math
def roots(a,b,c):
    d=round(b*b-4*a*c,2) 
    if d<0 :
        return None
    return round(-b/a,2) 
