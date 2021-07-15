from itertools import cycle

def decode(code, key):
    k = cycle( list(map(int, str(key))) )
    return ''.join( chr(96+c-next(k)) for c in code )
