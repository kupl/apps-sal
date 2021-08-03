def word_to_bin(w):
    return [format(ord(c), '08b') for c in w]
