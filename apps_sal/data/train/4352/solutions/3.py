def encrypt(text, rule):
    return ''.join((chr(ord(c) + rule & 255) for c in text))
