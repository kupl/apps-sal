def encrypt(text, key):
    return "".join(chr((ord(ch) + key) & 255) for ch in text)
