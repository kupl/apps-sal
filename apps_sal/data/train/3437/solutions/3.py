import re


def decipher_this(stg):
    return re.sub(r"(\d+)(\w?)(\w*)", decipher_word, stg)


def decipher_word(match):
    o, cl, cr = match.groups()
    return f"{chr(int(o))}{cr[-1:]}{cr[:-1]}{cl}"
