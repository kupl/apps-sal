from re import match

def is_hollow(x):
    return bool(match(r'(x*)[0]{3,}\1$', ''.join('x' if v else '0' for v in x)))
