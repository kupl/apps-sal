import math

def sillycase(silly):
    t=int(math.ceil(len(silly)/2.0))
    return silly[:t].lower() + silly[t:].upper()
