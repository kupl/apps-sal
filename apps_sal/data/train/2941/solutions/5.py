def add(*args):
    return round(sum(x/(c+1) for c,x in enumerate(args)))
