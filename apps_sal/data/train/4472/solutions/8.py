def bear_fur(bears):
    look = {('black', 'brown'): 'dark brown', ('black', 'white'): 'grey', ('brown', 'white'): 'light brown'}
    (b1, b2) = bears
    if b1 == b2 and b1 in {'black', 'brown', 'white'}:
        return b1
    return look.get(tuple(sorted([b1, b2])), 'unknown')
