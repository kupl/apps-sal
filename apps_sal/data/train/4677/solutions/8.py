from hashlib import md5

def crack(hash):
    for i in range(10 ** 5):
        s = b"%05d" % i
        if md5(s).hexdigest() == hash:
            return s.decode()
