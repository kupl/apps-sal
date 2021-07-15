def check(a, x): 
    if type(a) == 'string' and type(x) == 'string':
        return x.lower() in a
    else:
        return x in a
