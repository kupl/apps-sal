import math  

def ellipse(a, b):

    e = math.pi*(a*b)
    
    v = a**2+b**2
    
    p = math.pi*(3/2*(a+b)-math.sqrt(a*b))
    
    return "Area: {}, perimeter: {}".format(round(e,1),round(p,1))
    

