def word_to_bin(word):
    return [format(ord(c), '08b') for c in word]
