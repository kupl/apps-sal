vert_mirror = lambda S   : '\n'.join(s[::-1] for s in S.split('\n'))
hor_mirror  = lambda S   : '\n'.join(S.split('\n')[::-1])
oper        = lambda f, S: f(S)
