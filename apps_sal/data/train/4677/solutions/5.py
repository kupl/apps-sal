from hashlib import md5


def crack(hash):
    for pin in [str(x).rjust(5, '0') for x in range(0, 100000)]:
        if md5(pin.encode()).hexdigest() == hash:
            return pin
