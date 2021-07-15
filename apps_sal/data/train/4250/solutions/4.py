import hashlib
import itertools
def hashit(str):
    result = hashlib.sha256(str.encode())
    return result.hexdigest()
def guess(chars):
    yield from list(itertools.permutations(chars,len(chars)))
def sha256_cracker(hash, chars):
    for x in guess(chars):
        str = ''.join(x)
        if (hashit(str) == hash):
            return str
    return None
