def print_nums(*args):
    z = len(str(max(args))) if args else 0
    return '\n'.join((str(n).zfill(z) for n in args))
