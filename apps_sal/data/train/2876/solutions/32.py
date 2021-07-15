def check(a, x): 
    return x.lower() or x.upper() in a if type(a[0]) == 'str' and type(x) == 'str' else x in a
