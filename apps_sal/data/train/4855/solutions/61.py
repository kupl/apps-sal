def vert_mirror(string):
    return [s[::-1] for s in string]


def hor_mirror(string):
    return string[::-1]


def oper(fct, s):
    return '\n'.join(fct(s.split('\n')))
