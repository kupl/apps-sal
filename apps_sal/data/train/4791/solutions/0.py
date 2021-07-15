def word_to_bin(word):
    return ['{:08b}'.format(ord(c)) for c in word]
