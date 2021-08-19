(vert_mirror, hor_mirror, oper) = (lambda s: [e[::-1] for e in s], lambda s: s[::-1], lambda f, s: '\n'.join(f(s.split())))
