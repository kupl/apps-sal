from string import ascii_lowercase as abc


def encrypter(strng):
    return strng.translate(str.maketrans(abc[::-1], abc[13:] + abc[:13]))
