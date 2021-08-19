def word_to_bin(word):
    return ['{:0>8b}'.format(ord(c)) for c in word]
