abc = "abcdefghijklmnopqrstuvwxyz"


def keyword_cipher(s, keyword, key=""):
    for c in keyword + abc:
        if c not in key:
            key += c
    return s.lower().translate(str.maketrans(abc, key))
