from string import ascii_lowercase


def keyword_cipher(a, b):
    return a.lower().translate(str.maketrans(ascii_lowercase, ''.join(dict.fromkeys(b + ascii_lowercase))))
