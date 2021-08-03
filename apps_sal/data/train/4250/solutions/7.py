from hashlib import sha256
from itertools import permutations


def sha256_cracker(hash, chars):
    for x in map(''.join, permutations(chars)):
        if sha256(x.encode()).hexdigest() == hash:
            return x
