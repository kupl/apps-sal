from itertools import permutations
from hashlib import sha256


def sha256_cracker(hash, chars):
    return next(iter(''.join(p) for p in permutations(chars) if sha256(str.encode(''.join(p))).hexdigest() == hash), None)
