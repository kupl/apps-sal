def box(coords):
    xset,yset=set(),set()
    for x,y in coords:
        xset.add(x)
        yset.add(y)
    return {'nw':[max(xset),min(yset)],'se':[min(xset),max(yset)]}
