from re import findall
def decipher(cipher):
    return "".join(chr(int(d)) for d in findall("9\d|1[01]\d|12[012]",cipher))
