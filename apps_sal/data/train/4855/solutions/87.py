def vert_mirror(x): return '\n'.join([i[::-1] for i in x.split('\n')])
def hor_mirror(x): return '\n'.join(x.split('\n')[::-1])
def oper(x, y): return x(y)
