def word_to_bin(word):
    return [f'{ord(c):08b}' for c in word]
