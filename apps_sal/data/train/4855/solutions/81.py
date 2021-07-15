def vert_mirror(parts):
    return [p[::-1] for p in parts]

def hor_mirror(parts):
    return parts[::-1]

def oper(fct, s):
    parts = s.split('\n')
    return '\n'.join(fct(parts))
