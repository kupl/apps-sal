def maxlen(*args):
    x,y = sorted(args)
    return [y/2, x, y/3][ (y>2*x) + (y>3*x) ]
