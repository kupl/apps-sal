def print_nums(*args):
    return '\n'.join(['0'*(len(str(max(args)))-len(str(x)))+str(x) for x in args])
