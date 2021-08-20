from string import ascii_lowercase as al
tbl1 = str.maketrans(al, al[13:] + al[:13])
tbl2 = str.maketrans(al, al[::-1])


def encrypter(strng):
    return strng.translate(tbl1).translate(tbl2)
