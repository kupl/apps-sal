LEET_ALPHABET = '@8(D3F6#!JK1MN0PQR$7UVWXY2'

def to_leet_speak(str):
    return ''.join(LEET_ALPHABET[ord(c) - ord('A')] if c.isalpha() else c for c in str)
