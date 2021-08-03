def bear_fur(bears):
    s = set(bears)
    if s == {'black'}:
        return 'black'
    if s == {'brown'}:
        return 'brown'
    if s == {'white'}:
        return 'white'
    if s == {'black', 'brown'}:
        return 'dark brown'
    if s == {'black', 'white'}:
        return 'grey'
    if s == {'brown', 'white'}:
        return 'light brown'
    return 'unknown'
