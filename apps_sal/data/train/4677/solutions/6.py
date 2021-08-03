import hashlib


def crack(hash):
    for i in range(0, 99999):
        pin = digit_to_pin(i).encode()
        rand_hash = hashlib.md5(pin).hexdigest()
        if hash == rand_hash:
            return pin.decode()
        else:
            pass


def digit_to_pin(digit):
    string = str(digit)
    if len(string) < 5:
        nulls = (5 - len(string)) * "0"
        string = nulls + string
    return string
