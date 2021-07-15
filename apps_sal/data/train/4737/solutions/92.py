def fuel_price(l,p):
    """ Candian Gas Sale"""
    return round(l*(p-(l//2 *.05)),2) if l <12 else round(l*(p-.25) ,2)

