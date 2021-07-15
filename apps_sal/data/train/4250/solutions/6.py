from itertools import permutations
from hashlib import sha256

def sha256_cracker(hash, chars):
  return next(("".join(p) for p in permutations(chars) if sha256("".join(p).encode('utf-8')).hexdigest() == hash), None)
