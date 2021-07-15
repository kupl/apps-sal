def arithmetic(a, b, operator):
    d = dict()
    d["add"] = '+'
    d["subtract"] = '-'
    d["multiply"] = '*'
    d["divide"] = '/'
    
    return eval('{0} {1} {2}'.format(a, d[operator], b))
