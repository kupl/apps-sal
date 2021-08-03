import hashlib
import itertools


def sha256_cracker(hash, chars):
    for p in itertools.permutations(chars):
        if(toSHA256("".join(p)) == hash):
            return "".join(p)
    return None


def toSHA256(s):
    m = hashlib.sha256()
    m.update(s.encode())
    return m.hexdigest()
