import hashlib
from itertools import permutations

def sha256_cracker(hash, chars):
    bs = chars.encode()
    h = bytes.fromhex(hash)
    return next((
        bytes(xs).decode()
        for i in range(1, min(10, len(bs))+1)
        for xs in permutations(bs, i)
        if hashlib.sha256(bytes(xs)).digest() == h
    ), None)
