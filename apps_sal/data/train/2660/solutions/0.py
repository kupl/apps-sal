def args_to_string(args):
    L = []
    for arg in args:
        if isinstance(arg, str):
            L.append(arg)
        elif len(arg) == 1:
            L.append(arg[0])
        elif len(arg[0]) == 1:
            L.append('-' + ' '.join(arg))
        else:
            L.append('--' + ' '.join(arg))
    return ' '.join(L)
