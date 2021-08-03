import hashlib


def crack(hash):
    return [str(x) for x in range(100000) if hashlib.md5(('{0:05}'.format(x)).encode()).hexdigest() == hash][0].zfill(5)
