import hashlib
def crack(hash):
    for i in range(100000):
        if hashlib.md5(str(i).zfill(5).encode()).hexdigest() == hash:
            return str(i).zfill(5)
