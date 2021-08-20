from string import ascii_letters, digits
from collections import Counter
ALPHABET = ascii_letters + digits
C_ALPHABET = Counter(ALPHABET)


def blocks(s):
    d = Counter(ALPHABET + s) - C_ALPHABET
    return '-'.join((''.join((x for x in d if d[x] > i)) for i in range(max(d.values(), default=0))))
