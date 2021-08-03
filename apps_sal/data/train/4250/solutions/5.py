import hashlib
from itertools import permutations


def sha256_cracker(code, chars):
    x = [''.join(i) for i in permutations(chars)]
    for i in x:
        if hashlib.sha256(str.encode(i)).hexdigest() == code:
            return i
