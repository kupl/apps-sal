def args_to_string(args):
    params = []
    for arg in args:
        if isinstance(arg, str):
            params.append(arg)
        elif arg:
            first = arg.pop(0)
            if arg:
                if len(first) == 1:
                    first = '-' + first
                else:
                    first = '--' + first
            params.append(first)
            for a in arg:
                params.append(a)
    return ' '.join(params)
