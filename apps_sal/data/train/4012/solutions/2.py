from string import ascii_letters
import numpy as np

def encrypt(text, key):
    # Character and interger conversions
    code = lambda s: ord(s.lower()) - ord('a')
    letter = lambda n: chr(n + ord('A'))

    # Build key
    size = int(len(key) ** 0.5)
    if size ** 2 != len(key):
        raise ValueError('Key must be of length n^2')    
    key_matrix = np.array([code(c) for c in key]).reshape(size, size)
    
    # Filter out non letters and pad if necessary
    text = ''.join(c for c in text if c in ascii_letters)
    if len(text) % size != 0:
        text += 'z' * (size - (len(text) % size))
    text_matrix = np.array([code(c) for c in text]).reshape(len(text) // size, size).transpose()
    
    # Perform encoding
    encoded = (key_matrix @ text_matrix) % 26
    return ''.join(letter(n) for n in encoded.transpose().flatten())

