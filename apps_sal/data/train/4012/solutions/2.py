from string import ascii_letters
import numpy as np


def encrypt(text, key):
    def code(s): return ord(s.lower()) - ord('a')
    def letter(n): return chr(n + ord('A'))

    size = int(len(key) ** 0.5)
    if size ** 2 != len(key):
        raise ValueError('Key must be of length n^2')
    key_matrix = np.array([code(c) for c in key]).reshape(size, size)

    text = ''.join(c for c in text if c in ascii_letters)
    if len(text) % size != 0:
        text += 'z' * (size - (len(text) % size))
    text_matrix = np.array([code(c) for c in text]).reshape(len(text) // size, size).transpose()

    encoded = (key_matrix @ text_matrix) % 26
    return ''.join(letter(n) for n in encoded.transpose().flatten())
