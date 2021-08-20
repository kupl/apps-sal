def word_to_bin(s):
    return ['{0:08b}'.format(ord(c)) for c in s]
