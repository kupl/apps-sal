from collections import Counter
from string import ascii_lowercase

def decrypt(test_key):
    c = Counter(test_key)
    return ''.join(str(c[x]) for x in ascii_lowercase)

