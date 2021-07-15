vert_mirror = lambda x:'\n'.join([i[::-1] for i in x.split('\n')])
hor_mirror = lambda x: '\n'.join(x.split('\n')[::-1])
oper = lambda x, y: x(y)
