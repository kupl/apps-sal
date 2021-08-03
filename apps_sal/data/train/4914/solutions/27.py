from string import ascii_lowercase as lc


def position(alphabet):
    return f'Position of alphabet: {lc.find(alphabet.lower()) + 1}'
