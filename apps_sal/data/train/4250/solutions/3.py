from hashlib import sha256
from itertools import permutations as p
def sha256_cracker(h, c): return next((''.join(i) for i in p(c) if sha256(''.join(i).encode()).hexdigest() == h), None)
