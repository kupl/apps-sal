from math import ceil 

def get_participants(hs):
    return ceil((1+(1+8*(hs))**.5)/2)
