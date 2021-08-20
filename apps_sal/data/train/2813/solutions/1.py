import string
letters = string.ascii_lowercase[::-1] + '!? '


def switcher(arr):
    return ''.join([letters[ch - 1] for ch in map(int, arr) if ch])
