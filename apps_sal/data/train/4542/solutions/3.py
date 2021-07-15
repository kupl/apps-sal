from string import ascii_lowercase as al, ascii_uppercase as au
a = au + al

def caesar_crypto_encode(text, shift):
    text = (text or '').strip()
    shift %= 52
    tbl = str.maketrans(a, a[shift:]+a[:shift])
    return text.translate(tbl)
