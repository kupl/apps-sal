def double_char(s):
    return reduce(lambda x,y: x+y, map(lambda x : 2*x, s))
