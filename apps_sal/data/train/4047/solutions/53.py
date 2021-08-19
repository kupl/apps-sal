from string import ascii_uppercase


def to_leet_speak(str):
    trans = str.maketrans(ascii_uppercase, '@8(D3F6#!JK1MN0PQR$7UVWXY2')
    return str.translate(trans)
