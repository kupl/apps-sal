vert_mirror = lambda s: '\n'.join(r[::-1] for r in s.split('\n'))
hor_mirror = lambda s: '\n'.join(s.split('\n')[::-1])
oper = lambda f, s: f(s)
