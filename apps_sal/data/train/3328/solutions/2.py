import string

def caeser(message, key):
    return ''.join([chr((ord(s.upper()) + key - 65) % 26 + 65) if s in string.ascii_lowercase else s for s in message])
