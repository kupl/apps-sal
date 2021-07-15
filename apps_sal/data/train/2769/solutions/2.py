import re
def decipher(cipher):
    return re.sub('1?\d{2}',lambda m:chr(int(m.group())),cipher)
