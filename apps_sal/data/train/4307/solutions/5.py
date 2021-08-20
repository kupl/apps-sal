def unused_digits(*args):
    s = ''.join((str(a) for a in args))
    return ''.join((c for c in '0123456789' if c not in s))
