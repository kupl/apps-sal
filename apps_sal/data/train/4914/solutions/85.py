from string import ascii_lowercase as alphabet


def position(letter):
    return 'Position of alphabet: {}'.format(alphabet.find(letter) + 1)
