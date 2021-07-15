import math
import decimal
def weight(n, w):
    weight = 0
    i0 = 0.14849853757254047
    
    ##constant estimated by dividing two integrals
    fundamental_constant_of_glass_windows = 0.135335283237
    
    while n >= 0:
        weight += ((i0)*(fundamental_constant_of_glass_windows**n)) * w
        n -= 1
    return weight
    
    # if something is extremly dumb but it works, it isn't dumb

