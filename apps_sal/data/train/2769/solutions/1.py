import re

def decipher(cipher):
    return re.sub(r'1?\d\d', lambda m: chr(int(m.group())), cipher)

