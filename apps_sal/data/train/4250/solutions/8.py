from hashlib import sha256
from itertools import permutations


def sha256_cracker(hash, chars):
    for stg in (''.join(p) for p in permutations(chars)):
        if sha256(stg.encode('utf-8')).hexdigest() == hash:
            return stg
