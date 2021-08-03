def print_nums(*args):
    width = max((len(str(num)) for num in args), default=0)
    return '\n'.join('{:0{}d}'.format(num, width) for num in args)
