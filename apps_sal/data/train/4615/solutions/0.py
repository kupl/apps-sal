def logistic_map(width,height,xs,ys):
    return [ [ min([abs(x-x2)+abs(y-ys[i]) for (i,x2) in enumerate(xs)]) if len(xs) else None for x in range(width) ] for y in range(height) ]
