from hashlib import sha256
from itertools import permutations


def sha256_cracker(hash, chars):
    for p in permutations(chars, len(chars)):
        current = ''.join(p)
        if sha256(current.encode('utf-8')).hexdigest() == hash:
            return current
