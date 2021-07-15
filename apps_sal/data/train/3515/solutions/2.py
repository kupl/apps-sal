import re
from string import ascii_lowercase as alphabet

def keyed_alphabet(key):
    char2idx, idx2char = {}, {}
    for letter in key + alphabet:
        if letter not in char2idx:
            char2idx[letter] = len(char2idx)
            idx2char[len(idx2char)] = letter
    return char2idx, idx2char

def ragbaby(mode, text, key):
    char2idx, idx2char = keyed_alphabet(key)
    cipher_word = lambda match: ''.join(
    [str.upper, str.lower][letter.islower()](idx2char[(char2idx[letter.lower()] + idx * mode) % len(alphabet)])
            for idx, letter in enumerate(match.group(), 1))
    return re.sub('[{}]+'.format(alphabet), cipher_word, text, flags=re.I)

encode, decode = lambda *args: ragbaby(1, *args), lambda *args: ragbaby(-1, *args)
