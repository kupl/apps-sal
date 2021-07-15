def closest_pair_tonum(uLim):
    return next( (a,b) for a in reversed(range(1,uLim)) for b in reversed(range(1,a))
                       if not (a+b)**.5%1 and not (a-b)**.5%1 )
