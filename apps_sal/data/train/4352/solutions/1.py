def encrypt(text, rule):
    return "".join(chr((ord(c) + rule) % 256) for c in text)
