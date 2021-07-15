from collections import Counter
from string import ascii_lowercase

def decrypt(test_key):
    return ''.join(map(str, map(Counter(test_key).__getitem__, ascii_lowercase)))
