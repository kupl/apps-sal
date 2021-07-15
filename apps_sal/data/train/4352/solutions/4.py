def encrypt(text, rule):
    return ''.join([chr((ord(a) + rule) % 256) for a in text])
