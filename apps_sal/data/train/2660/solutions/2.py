def args_to_string(args):
    return ' '.join((x if type(x) == str else ' '.join((('-' if len(v) == 1 else '--') + v if k == 0 and len(x) > 1 else v for (k, v) in enumerate(x))) for x in args))
