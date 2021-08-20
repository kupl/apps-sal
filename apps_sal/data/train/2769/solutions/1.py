import re


def decipher(cipher):
    return re.sub('1?\\d\\d', lambda m: chr(int(m.group())), cipher)
