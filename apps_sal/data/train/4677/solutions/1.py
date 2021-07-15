from hashlib import md5
from itertools import product

def crack(hash):
    for bs in map(bytes, product(b'0123456789', repeat=5)):
        if md5(bytes(bs)).hexdigest() == hash:
            return bs.decode()
