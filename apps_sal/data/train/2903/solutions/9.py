def volume(r,h):
    
# =============================================================================
#     This function calculates the Volume of a cone using the formulae 
#     π x r² x h/3, and returns the result as a rounded down integer.
# =============================================================================

    import math
    
    return math.floor(math.pi * r**2 * h/3)
