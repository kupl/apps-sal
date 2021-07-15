def add(*args):
    return sum((i+1)*v for i,v in enumerate(args))
