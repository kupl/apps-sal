def print_nums(*args):
    max_len = max([len(str(n)) for n in args]) if len(args) > 0 else 0
    return '\n'.join(('0' * (max_len - len(str(n))) + str(n) for n in args))
