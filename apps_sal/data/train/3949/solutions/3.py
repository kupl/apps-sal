import math
def calculate_tip(a, r):
    return {"terrible":0*a,"poor":math.ceil(0.05*a),"good":math.ceil(0.1*a),"great":math.ceil(0.15*a),"excellent":math.ceil(0.2*a)}.get(r.lower(), "Rating not recognised")
