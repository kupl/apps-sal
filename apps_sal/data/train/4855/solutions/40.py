def vert_mirror(S):
    return '\n'.join((s[::-1] for s in S.split('\n')))


def hor_mirror(S):
    return '\n'.join(S.split('\n')[::-1])


def oper(f, S):
    return f(S)
