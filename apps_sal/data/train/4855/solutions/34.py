def vert_mirror(s):
    return '\n'.join(list(map(lambda x: x[::-1], s.split('\n'))))


def hor_mirror(s):
    return '\n'.join(s.split('\n')[::-1])


def oper(f, s):
    if str(f).split()[1] == 'vert_mirror':
        return vert_mirror(s)
    return hor_mirror(s)
