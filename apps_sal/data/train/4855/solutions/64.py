def vert_mirror(value: str):
    return '\n'.join([s[::-1] for s in value.split('\n')])


def hor_mirror(value):
    return '\n'.join(value.split('\n')[::-1])


def oper(func, value):
    return func(value)
