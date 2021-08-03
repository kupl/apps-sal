def encrypt(text, rule):
    return "".join(chr((ord(x) + rule) % 256) for x in text)
