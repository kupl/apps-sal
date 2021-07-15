def encrypt(text, rule):
    return ''.join([chr((ord(s) + rule) % 256) for s in text])
