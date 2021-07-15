from string import ascii_lowercase as al

def position(alphabet):
    return f'Position of alphabet: {[pos for pos, x in enumerate(al, 1) if x == alphabet.lower()][0]}'
