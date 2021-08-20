(hor_mirror, vert_mirror, oper) = (reversed, lambda m: map(reversed, m), lambda f, s: '\n'.join(map(''.join, f(s.split('\n')))))
