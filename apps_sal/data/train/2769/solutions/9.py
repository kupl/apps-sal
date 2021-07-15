import re

def decipher(cipher):
    return ''.join(chr(int(x)) for x in re.findall(r'1\d\d|\d\d', cipher))
