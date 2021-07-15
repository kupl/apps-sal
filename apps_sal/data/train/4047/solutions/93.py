from string import ascii_uppercase
L = str.maketrans(ascii_uppercase, '@8(D3F6#!JK1MN0PQR$7UVWXY2')

to_leet_speak = lambda s: s.translate(L)
