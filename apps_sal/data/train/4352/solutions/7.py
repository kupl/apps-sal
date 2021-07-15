def encrypt(text, rule):
    return ''.join(map(lambda x: chr((ord(x)+rule)%256), text))
